# Amadeus GDS — Interactive Interview Study Guide

A single, self-contained interactive study guide built from the "Training Notes" email
(an Amadeus interview-prep note). It turns every cryptic command and all 7 attached screenshots
into searchable cards, decision matrices, annotated terminal captures, charts, flashcards and a quiz.

Everything — HTML, CSS, JavaScript and all 7 images (embedded as base64 data URIs) — lives in the
**single `index.html` file**. There are no separate JS, CSS, or image files and no external/CDN
dependencies.

## Open it

Just double-click / open `index.html` in any modern browser — no build step, no dependencies,
fully offline (`file://` works). You can also email or share the one file as‑is.

```bash
# optional: serve locally
cd amadeus-study-guide
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Navigation

The guide shows **one section at a time** (a wizard). Move between sections with the
**Previous / Next** bar at the bottom, the **left sidebar**, or the **← / →** arrow keys.

## What's inside

- **Encode / Decode** (`DAN`, `DAC`, `DNA`, `DNE`, `DC`, `GG COU`, `DNS`, `GG APT`, `HEDD`)
- **Time & Zulu** (`DD`, `DDZZZ`, time-difference / specific-time entries)
- **Availability & Schedules** (`SN` vs `AN`, cabin `/K` filters, transit `/X`, airline filters, `SCR`, `MPSN`)
- **RBD / cabin classes** ladder (`/KF /KC /KW /KY /KM`)
- **Creating a PNR** (mandatory elements, `SS`, `SB`, `RTRN`, MCT `DM`)
- **Seats & SSR** (`ST/NSSA`, `ST/NSSW`, `RTSTR`)
- **Pricing** decision matrix (`FXP / FXX / FXB / FXR / FXA`, `FXT`, `FXU`, `FXY`, `TTE`, `FQN`)
- **Fare families** (`FQF`, `FQQ`, `FXU`, `/FF-`), with charts from the real screenshots
- **Pricing filters** (`/KC`, `/K-`, `/SBF`, flexibility `*NPE/*RF/*RB/*NR`)
- **Currency & FQD** (`FQC`, `FQD…/FS-`, `FQP`)
- **Round-the-world** (`FXA…/S2RW`, `FQDBKKBKK…`)
- **ATC / Reissue** matrix (`FXQ / FXO / FXF / FXE`, workflow, `TTP`, `FQR`, `IR`)
- **Ticketing & EMD** (`TGGSD`, `VC`, `TTP/TTM`, `EGSD`, `TWD/O`, `HE ETT`)
- **Hotels** and **Cars** Amadeus Assistant cheat sheets + car-type code decoder
- **Command finder** (searchable, filterable), **flashcards**, and a **10-question quiz**

## Source screenshots

All 7 original email attachments are embedded directly in `index.html` (base64 data URIs) and
annotated in context — no external image files are required.
