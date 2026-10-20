# YGOlookup

A Yu-Gi-Oh! card lookup that is one single file and works without internet. The full database is in the HTML file.

Search any of 13,000 or more cards, read the full card, and see its Genesys point
value and its TCG Forbidden & Limited status together in one place.

---

## Get started

1. Download the `.html` file from the Releases page.
2. Open it. Double-click it, or drag it into a browser window.

That is all. There is no installation, no account, and no set-up.

The file name tells you which release you have. For example,
`ygolookup-v1.9.html` is release 1.9.

The bottom of the screen tells you how fresh the card data is. It reads
something like `13,892 cards · data 16 Sep 2026 · DB 147.04 · v1.9`. The date is
the day YGOPRODeck last changed the card database that this release was built
from.

### Keep it on your phone

- **iPhone or iPad**: save the file to the Files app. Open it from there. You can
  also open it in Safari and add it to your Home Screen.
- **Android**: save the file to your Downloads folder and open it with Chrome.

---

## It works with no internet

All of the card data is inside the file. Nothing is downloaded when you use it.

This means:

- It works on a plane, on a train, in a basement, and at a tournament venue with
  no signal.
- It is fast. There is no wait for a server.
- Nothing about your searches leaves your device.

The file is about 1.5 MB, which is smaller than one photograph.

Only the three buttons below a card need the internet. They are ordinary web
links. Everything else keeps working with no connection.

---

## Search

Type in the box in the middle of the screen. A list of matches appears as you
type.

**You do not have to type the name correctly.**

- Punctuation does not matter. Type `harpies feather duster` to find
  *Harpie's Feather Duster*.
- Word order does matter, but missing words do not. Type `harpie duster` and you
  will still find it.
- Capital letters do not matter.

**You can search the card text, not only the name.** Type `draw 2 cards` to find
every card that says that. Type `banish` to find every card that banishes.

**You can search a card's properties.** Type `zombie` to find Zombie monsters.
Type `quick-play` to find Quick-Play Spells. Type `forbidden` to find cards on
the Forbidden list.

### How the list is sorted

The closest matches come first:

1. The exact name
2. Names that start with what you typed
3. Names that contain what you typed
4. Cards whose type, attribute, or list status matches
5. Cards whose card text matches

Inside each group, cards are in alphabetical order.

### See every match

The drop-down list shows the first 25 matches. Press **Enter** to see the full
list. The full list shows up to 300 cards and tells you the true total.

Touch any row to open that card.

---

## Filters

Touch **Filters** below the search box.

You can filter by card type, attribute, monster type, level or rank, Pendulum
scale, Link rating, Link arrows, Spell kind, Trap kind, ATK, DEF, Forbidden &
Limited status, and Genesys points.

### Keep or remove

Each button has three states. Touch it again to move to the next state.

| Touches | Colour | Result |
|---|---|---|
| Once | Gold | Keep **only** cards with that value |
| Twice | Red, crossed out | Remove **all** cards with that value |
| Three times | Plain | No effect |

So you can ask for "all DARK monsters that are **not** Dragons" — touch `DARK`
once and touch `Dragon` twice.

### ANY or ALL

Card Type and Link Arrows have an **ANY / ALL** button. A card can have more than
one of these, so you get to choose what a group of selections means.

- **ANY**: the card needs at least one of the values you chose.
- **ALL**: the card needs every value you chose.

Touch `Tuner` and `Synchro` with **ANY** and you get about 1,070 cards. Change it
to **ALL** and you get 59 — only the monsters that are both.

The ANY/ALL button does not change what "remove" means. A removed value is always
removed.

### ATK and DEF

Type a smallest value, a largest value, or both. Leave a box empty for no limit.

Some cards have `?` for ATK or DEF. These are left out unless you tick
**Include ? ATK** or **Include ? DEF**.

### Other notes about filters

- Filters and typed words work together. Type `dragon`, then filter to LIGHT and
  Level 8, and you get only the cards that satisfy all three.
- The Filters button shows how many filters you have set.
- The bottom of the panel shows how many cards match, and it updates as you go.
- **Clear all filters** puts everything back.

---

## Reading a card

The card is drawn the way it looks in your hand, without the picture and without
the set code.

- **The disc in the top right** is the attribute, written as a word: DARK, LIGHT,
  EARTH, WATER, FIRE, WIND, DIVINE. Spells show SPELL and Traps show TRAP.
- **LEVEL 8** is on the left with the stars on the right. Xyz monsters are the
  mirror image: the stars are on the left and **RANK 4** is on the right.
- **The line in brackets** gives the type. Monsters read `[ Dragon / Normal ]`.
  Spells and Traps use the same shape: `[ Spell / Equip ]`,
  `[ Trap / Counter ]`.
- **Link monsters** show their arrows on the card edge and their rating in the
  bottom corner, in place of DEF.
- **Pendulum monsters** show the two text boxes separately, with the blue and red
  scale values at the sides.

### The two circles

These are not printed on a real card. They are added for you.

- **The blue circle in the top left** is the card's Genesys point value. It
  appears only if the card has points.
- **The red circle in the top right** is the TCG Forbidden & Limited status. A
  crossed circle is Forbidden, **1** is Limited, and **2** is Semi-Limited. An
  unlimited card shows nothing, the same as a real card.

The line below the card always gives both values in words, including the ones
that show no circle.

### Go back

Touch the black space around the card to go back to your list of results.

---

## The three buttons below a card

These open the card on other websites. They need the internet.

- **YGOPRODeck** — the card page, with prices and decks that use it
- **Yugipedia** — the wiki page, with rulings, artwork, and history
- **TCGplayer** — a search for that card, to buy it

---

## What is in the file, and what is not

**In the file**

- Every card released in the TCG: 13,000 or more
- Name, card type, monster type, attribute, level or rank, ATK, DEF, Pendulum
  scale, Link rating, Link arrows
- The full card text, including both text boxes on Pendulum cards
- TCG Forbidden & Limited status
- Genesys point values

**Not in the file**

- Card pictures. They would make the file more than ten times larger.
- Set codes and print runs.
- Prices. These change every day, so they cannot be stored offline. Use the
  TCGplayer button.
- OCG cards, and the OCG and GOAT Forbidden & Limited lists. This tool is for the
  TCG.
- Skill Cards and Tokens. These are not TCG deck cards.
- A deck builder or a collection tracker. This tool only looks cards up.

---

## What you need

Any browser from 2023 or later. That covers:

- Safari 16.4 or later, on macOS, iOS, and iPadOS
- Chrome, Edge, Brave, and other Chrome-based browsers
- Firefox

The card data is packed to keep the file small, and the browser unpacks it when
the page opens. This takes well under a second. An older browser cannot unpack
it, and the page will tell you so rather than fail quietly.

---

## Releases

A job runs every day. It asks YGOPRODeck whether the card database has changed.
If it has, it builds a new file and publishes it. If it has not, it does
nothing, so there is no release on days when no card data moved.

Each release is named after the card data it holds, for example
`Card data 147.04 (16 Sep 2026)`. Take the newest one.

If you clear the search box while a filter is still set, the filtered list
stays on screen. Use **Clear all filters** to start over.

---

## Where the data comes from

All card data comes from the [YGOPRODeck](https://ygoprodeck.com) public API.
Thank you to YGOPRODeck for making it available.

Each release is built from the database on one particular day. That date is at
the bottom of the screen. New cards and new Forbidden & Limited lists appear
only in a new release.

Genesys point values also come from YGOPRODeck, and they change as the format
changes. Always check a current release before you build for an event.

---

## Questions

**Is my old file still good?**
Yes. It keeps working. It just holds the card data from the day it was built.

**Why is there no picture?**
Pictures would make the file about ten times larger and would need the internet
to load. Use the YGOPRODeck button to see the artwork.

**A card is missing.**
It is probably too new for your release, or it is an OCG card that the TCG has
not had yet. Try a newer release.

**The Genesys number looks wrong.**
Genesys points change with the format. Check the date at the bottom of the
screen. If it is older than the last Genesys update, get a newer release.

**Can I put this on my own website?**
Yes. It is one file with nothing else attached. Upload it anywhere.

---

## A note

This is an unofficial fan project. It is not made by, approved by, or connected
to Konami. Yu-Gi-Oh! is a trademark of its owner.
