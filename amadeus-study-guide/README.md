# Amadeus GDS — Interactive Interview Study Guide

A single-page, self-contained interactive study guide built from the "Training Notes" email
(an Amadeus interview-prep note). It turns every cryptic command and all 7 attached screenshots
into searchable cards, decision matrices, annotated terminal captures, charts, flashcards and a quiz.

## Open it

Just open `index.html` in any modern browser — no build step, no dependencies, works offline
(`file://` is fine). Images live in `assets/`.

```bash
# optional: serve locally
cd amadeus-study-guide
python3 -m http.server 8000
# then visit http://localhost:8000
```

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

`assets/image001…007` are the original attachments from the email, annotated in context.
