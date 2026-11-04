#!/usr/bin/env python3
"""Search Code_Library's vetted source catalog without importing project source."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    if catalog.get("schema") != 1 or not isinstance(catalog.get("items"), list):
        raise ValueError("Unsupported catalog schema")
    return catalog["items"]

def search(items, query, category=None):
    words = query.lower().split()
    matches = []
    for item in items:
        if category and item.get("category") != category:
            continue
        haystack = " ".join(str(v) for v in item.values()).lower()
        if all(word in haystack for word in words):
            matches.append(item)
    return matches

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--category", default=None)
    parser.add_argument("--limit", type=int, default=15)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    hits = search(load(), args.query, args.category)[:max(0, min(args.limit, 100))]
    if args.json:
        print(json.dumps(hits, indent=2))
    else:
        for x in hits:
            ref = x.get("source_ref", "main")
            url = "https://github.com/" + x["source_repo"] + "/blob/" + ref + "/" + x["source_path"]
            print(f'{x["id"]} [{x["status"]}] — {x["purpose"]}\n  {url}')
        print(f"{len(hits)} candidate(s). Sources require independent review before reuse.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
