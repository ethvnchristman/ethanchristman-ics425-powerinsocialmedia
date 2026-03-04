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

Each stakeholder is scored across three dimensions (0–10):

- **data_access** — visibility into platform data and behavioral profiles
- **revenue_share** — share of platform-generated revenue
- **decision_power** — influence over platform rules and algorithm

An **autonomy score** is automatically calculated as the mean of these three values.

---

## Proposed Classes

| Existing | Proposed |
|----------|----------|
| `User` | `EmpoweredUser` |
| `Creator` | `EmpoweredCreator` |
| `PlatformOwner` | `AccountablePlatform` |

---

## Migration Functions
```python
migrate_user_to_empowered(old_user)
migrate_creator_to_empowered(old_creator)
migrate_platform_to_accountable(old_platform)
```

Each function takes an instance of the existing class, preserves its name, and returns an instance of the proposed class — printing a before/after diff of all power attributes.

---

## Context

This project accompanies the *Power in Social Media* written report analyzing TikTok's stakeholder ecosystem. The three proposed modifications modeled in code are:

1. **Data portability rights** for users
2. **Transparent, fixed revenue splits** for creators
3. **Independent algorithmic oversight** of the platform

---

*ICS 425 — Ethan C. | University of Hawaii at Manoa*
