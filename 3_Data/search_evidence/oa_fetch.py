import json, urllib.request, urllib.parse, time, datetime
Q = {
 "Q1": '("sentiment analysis" OR "opinion mining" OR "text mining" OR "topic modeling" OR "topic modelling") AND (airline OR airlines OR "air passenger" OR "air passengers" OR airport OR "air travel")',
 "Q2": '("concept drift" OR "data drift" OR "temporal drift" OR "semantic drift" OR "sentiment drift" OR "temporal persistence") AND ("sentiment" OR "text classification" OR "text stream" OR "natural language processing")',
 "Q3": '("MLOps" OR "machine learning operations" OR "human-in-the-loop") AND ("concept drift" OR "model monitoring" OR "quality assurance" OR "retraining")',
}
def get(u):
    for a in range(6):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "slr/1.0"}), timeout=90))
        except Exception as e: print("retry", getattr(e, "code", e)); time.sleep(10 * (a + 1))
    raise SystemExit("failed " + u)
out = {"run_date": datetime.date.today().isoformat(), "queries": Q, "records": {}}
for k, q in Q.items():
    f = f"title_and_abstract.search:{q},publication_year:2021-2026,language:en,type:article|review"
    page, recs = 1, []
    while True:
        u = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": f, "per-page": 100, "page": page, "select": "id,doi,title,publication_year,type,primary_location,abstract_inverted_index,authorships"})
        d = get(u); page += 1
        for w in d["results"]:
            inv = w.get("abstract_inverted_index") or {}
            ab = " ".join(x for _, x in sorted((p, t) for t, ps in inv.items() for p in ps))
            src = ((w.get("primary_location") or {}).get("source") or {})
            recs.append({"id": w["id"], "doi": (w.get("doi") or "").replace("https://doi.org/", "").lower(), "title": w.get("title") or "", "year": w["publication_year"], "type": w["type"],
                         "venue": src.get("display_name") or "", "venue_type": src.get("type") or "", "issn": src.get("issn_l") or "",
                         "first_author": ((w.get("authorships") or [{}])[0].get("author") or {}).get("display_name", "") if w.get("authorships") else "", "abstract": ab})
        if not d["results"]: break
        time.sleep(3)
    out["records"][k] = recs; print(k, len(recs), "count", d["meta"]["count"])
json.dump(out, open("search_export.json", "w"))
