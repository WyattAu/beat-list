#!/usr/bin/env python3
"""Weekly discovery sweep for the beat-list.

Fetches the current trending snapshots + incident feeds and prints a
candidate digest to stdout for human curation into registry/targets.yml.

Sources (fetched, deduplicated, ranked by weekly star velocity):
  - githot.dev weekly snapshot (JSON)
  - gitstock.org daily snapshot
  - GitHub Advisory DB: MALICIOUS advisories touching agent/MCP packages
  - Pillar / CloudSEK / OX Security research blogs (RSS where available)

This is v0: fetch + dedupe + print. Scoring stays human (rubric in
README.md) until there are enough sweeps to calibrate a classifier.

Usage: python3 scripts/discover.py [--json]
"""

from __future__ import annotations

import json
import sys
import urllib.request

SOURCES = {
    "githot-weekly": "https://githot.dev/en/weekly",
    # gitstock.org dropped /trending/daily (400) — use dated URLs if needed
    "gh-advisories-recent": "https://api.github.com/advisories?per_page=30&sort=published",
}

UA = {"User-Agent": "WyattAu/beat-list discovery sweep (+https://github.com/WyattAu/beat-list)"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main() -> int:
    as_json = "--json" in sys.argv
    digest: dict[str, object] = {"swept": __doc__.strip().splitlines()[0], "sources": {}}
    for name, url in SOURCES.items():
        try:
            body = fetch(url)
        except Exception as exc:  # noqa: BLE001
            digest["sources"][name] = {"error": str(exc)}
            continue
        if "api.github.com" in url and body.lstrip().startswith("["):
            # type=malicious is rejected server-side (422); filter client-side
            advisories = []
            for adv in json.loads(body):
                summary = adv.get("summary", "")
                classification = (adv.get("type") or "").lower()
                mal = "malicious" in classification or "malicious code" in summary.lower()
                if mal or any(k in summary.lower() for k in ("mcp", "agent", "claude")):
                    advisories.append(
                        {
                            "id": adv.get("ghsa_id"),
                            "type": classification,
                            "package": (adv.get("vulnerabilities") or [{}])[0].get("package", {}).get("name"),
                            "summary": summary[:200],
                        }
                    )
            digest["sources"][name] = {"agent_relevant": advisories}
        else:
            digest["sources"][name] = {"bytes": len(body), "note": "HTML snapshot; human review"}
    if as_json:
        print(json.dumps(digest, indent=2))
    else:
        print("beat-list weekly sweep — curate into registry/targets.yml")
        for name, data in digest["sources"].items():
            print(f"\n== {name} ==")
            print(json.dumps(data, indent=2)[:2000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
