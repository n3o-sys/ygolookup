#!/usr/bin/env python3
"""Rebuild the offline YGOlookup page from the YGOPRODeck API.

Usage:  python3 update.py [--version 1.1]

Steps:
  1. Read checkDBVer.php to get the database version.
  2. Get cardinfo.php?misc=yes and cardinfo.php?format=genesys&misc=yes.
     Two requests, 0.25 s apart. The API limit is 20 requests each second.
     A breach blocks the IP address for 1 hour.
  3. Keep TCG releases only. Keep the display fields and the TCG banlist.
  4. Add the genesys points to each card that has a value.
  5. Compress with gzip, encode with base64, put it in template.html.
  6. Write ygolookup-v<version>.html next to this script.

template.html must sit in the same folder. It holds two markers,
__PAYLOAD__ and __META__.
"""
import argparse
import base64
import datetime
import gzip
import json
import os
import time
import urllib.request

API = "https://db.ygoprodeck.com/api/v7"
UA = "ygo-offline-lookup/1.0"
HERE = os.path.dirname(os.path.abspath(__file__))
DELAY = 0.25

KEEP = (("attribute", "a"), ("atk", "k"), ("def", "e"), ("level", "l"),
        ("linkval", "lv"), ("scale", "sc"), ("linkmarkers", "lm"),
        ("pend_desc", "pd"), ("monster_desc", "md"))


def get(path):
    req = urllib.request.Request(API + "/" + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.loads(r.read().decode("utf-8"))
    time.sleep(DELAY)
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="1.9")
    ap.add_argument("--print-db-version", action="store_true",
                    help="print the live database version and exit; used by CI "
                         "to skip a build when nothing has changed")
    args = ap.parse_args()

    ver = get("checkDBVer.php")[0]
    db = ver["database_version"]
    if args.print_db_version:
        print(db)
        return
    raw = ver["last_update"]                       # e.g. "2026-09-12 12:02:05"
    stamp = datetime.datetime.strptime(raw[:10], "%Y-%m-%d").strftime("%d %b %Y").lstrip("0")
    print("database version", db, "| last update", raw)

    cards = get("cardinfo.php?misc=yes")["data"]
    gen = get("cardinfo.php?format=genesys&misc=yes")["data"]
    print("cards from the API:", len(cards))

    points = {}
    for c in gen:
        v = c.get("misc_info", [{}])[0].get("genesys_points")
        if v:
            points[c["id"]] = v

    out = []
    for c in cards:
        if not c.get("misc_info", [{}])[0].get("tcg_date"):
            continue
        if c["frameType"] in ("skill", "token"):
            continue
        o = {"i": c["id"], "n": c["name"],
             "f": c["frameType"], "d": c.get("desc", "")}
        if c.get("typeline"):
            o["tl"] = c["typeline"]
        elif c.get("race"):
            o["r"] = c["race"]
        for src, dst in KEEP:
            if c.get(src) is not None:
                o[dst] = c[src]
        # A Link monster has no Level. The API still reports level 0 for them,
        # which would make all 108 of them answer the "Level 0" filter.
        if c["frameType"] == "link":
            o.pop("l", None)
        ban = c.get("banlist_info", {}).get("ban_tcg")
        if ban:
            o["b"] = ban
        if c["id"] in points:
            o["g"] = points[c["id"]]
        # ygoprodeck.com/card/<slug>-<n> redirects to ygoprodeck.com/card/<n>,
        # so only the trailing number is needed for the link.
        url = c.get("ygoprodeck_url") or ""
        tail = url.rsplit("-", 1)[-1]
        if tail.isdigit():
            o["y"] = int(tail)
        out.append(o)
    out.sort(key=lambda x: x["n"])

    raw = json.dumps(out, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    b64 = base64.b64encode(gzip.compress(raw, 9, mtime=0)).decode("ascii")

    tpl = open(os.path.join(HERE, "template.html")).read()
    meta = json.dumps({"db": db, "ver": args.version, "cards": len(out),
                       "updated": stamp},
                      separators=(",", ":"))
    html = tpl.replace("__PAYLOAD__", b64).replace("__META__", meta)

    name = "ygolookup-v%s.html" % args.version
    path = os.path.join(HERE, name)
    open(path, "w").write(html)
    print("TCG cards kept : %d" % len(out))
    print("with points    : %d" % sum(1 for x in out if x.get("g")))
    print("on the TCG list: %d" % sum(1 for x in out if x.get("b")))
    print("with a link id : %d" % sum(1 for x in out if x.get("y")))
    print("written        : %s  (%.2f MB)" % (name, os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main()
