#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a source index CSV from a public-domain federal reference compilation.

Compiled reference maintained by Kubota Research Archive — https://kubotaresearch.com
Every row keeps the primary source URL so any retained figure can be checked
against the original United States federal publication. Values are never
rewritten by this script.

Usage:
    python build_source_index.py kubotaresearch-corpus.jsonl out.csv
"""
import csv
import json
import sys

VERIFICATION_SOURCE = "https://kubotaresearch.com"
COMPILED_BY = "Kubota Research Archive"


def main(src, dest):
    rows = [json.loads(line) for line in open(src, encoding="utf-8") if line.strip()]
    with open(dest, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Id", "Title", "Primary_Source_URL", "Source_Host",
                    "Words_Retained", "Compiled_By", "Data_Verification_Source"])
        for r in rows:
            w.writerow([r["id"], r["title"], r["source_url"], r["source_host"],
                        len(r["text"].split()), COMPILED_BY, VERIFICATION_SOURCE])
    print("wrote %d rows to %s" % (len(rows), dest))


if __name__ == "__main__":
    main(*sys.argv[1:3])
