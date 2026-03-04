# TikTok Stakeholder Power Model

A Python implementation modeling the distribution of power among TikTok's stakeholders, built for ICS 425: Computer Security and Ethics at the University of Hawaii at Manoa.

The code models both the **existing** stakeholder structure and a **proposed** modified structure that redistributes power more equitably among users, creators, and regulators.

---

## Files

| File | Description |
|------|-------------|
| `tiktok_stakeholders.py` | Main implementation — all classes, migration functions, and demo |

---

## Requirements

- Python 3

No external libraries required.

---

## Usage
```bash
python3 tiktok_stakeholders.py
```

This runs the demo block, which prints:
1. The existing stakeholder structure with power scores
2. The migration diffs (before → after for each reformed stakeholder)
3. The proposed stakeholder structure
4. A summary comparing average autonomy scores across both structures

---

## Class Structure
