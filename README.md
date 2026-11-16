# CSC2102 Group Research Paper – Final Submission

**A PRISMA-Guided Systematic Review of Quality Assurance and Dynamic Concept Drift Monitoring for NLP Sentiment Models in Post-Pandemic Airline Passenger Analytics**

Asim Ali Khan (10412298) and Labeeb Mohsin (10446401) · CSC2102 AI and Data Science Project Management · Emirates Aviation University · Advisor: Dr. Zainab Rasheed · Fall 2026

| Folder | Contents |
|---|---|
| Paper | Submitted separately through Turnitin (not stored here) |
| `2_Presentation/` | PowerPoint slides with speaker notes |
| `3_Data/CSC2102_SLR_Data.xlsx` | Search queries, PRISMA counts (with check formulas), screening log of all 776 records, 25 included studies, quality scores, 34 full-text exclusions, synthesis tables, bibliography |
| `3_Data/search_evidence/` | Raw OpenAlex export (`search_export.json`, 787 records, run 10 Nov 2026), de-duplicated records (`unique.json`, 776) and the Python script that ran the search (`oa_fetch.py`) |
| `4_Bibliography/` | All 49 references, APA 7th edition |
| `5_Figures/` | Figure 1 PRISMA flow, Figure 2 studies by year and theme, Figure 3 DCDM protocol |

## Reproducing the search
`python3 oa_fetch.py` queries the OpenAlex API with the three search strings (title and abstract, 2021–2026, English, articles and reviews) and writes `search_export.json`. Counts will differ slightly if run on a later date because OpenAlex keeps indexing new work.

## PRISMA summary
787 records identified → 11 duplicates removed → 776 screened → 727 excluded → 49 sought (1 not retrieved) → 48 assessed → 30 excluded → 18 included from databases; 11 from citation searching, 4 excluded → 7 included. **Total: 25 studies.**
