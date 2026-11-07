# beat-list-campaign

status: active
updated: 2026-11-03  rev: 4

## State
| # | Task | Status | Evidence | Next |
|---|------|--------|----------|------|
| 1 | discovery sweep (trending + advisories) | done | sweep 2026-11-01, registry/targets.yml | weekly cadence |
| 2 | mcp-integrity-sentinel scored infra-critical | done | targets.yml score 15/15 | build approved |
| 3 | mcp-sentinel v0.1.0 (scan/pin/verify/verify-chain) | done | release v0.1.0 + SHA256SUMS on GH | remote probing (SSE/HTTP) |
| 4 | mcp-sentinel CI drift gate | done | ci.yml mutation roundtrip green on runners | auditlog export |
| 5 | mcp-guard Action into 4 forks | done | mcp-guard.yml in nightjar/outrider/offcut/dissect | adoption tracking |
| 6 | nightjar R0 + transcription verified on-box | done | docs/M1-WAYLAND-PLAN.md smoke results + headless RTF 0.22x | M1 voice tests (user) |
| 6b | mcp-sentinel v0.1.1 watch daemon | done | commit 8fed567, tag pushed | auditlog export |
| 7 | offcut zero-key transcription E2E | done | docs/M2-E2E-RUNBOOK.md 2026-11-02 entry | selection-stage model decision (user) |
| 8 | offcut full-pipeline E2E | blocked | docs/M2-E2E-RUNBOOK.md: triple-confirmed CPU model-capacity ceiling (tinyllama timeout, qwen0.5b + llama3.2:3b schema failures) | user: ROCm GPU / llama3.2:3b+3600s / flash-tier key |
| 9 | dissect v0.1.0 tag | blocked | docs/RELEASE.md written | user: GPG key fingerprint |
| 10 | outrider R2 platform depth | queued | — | after flagship M1 |

## Next action
Nightjar M1 voice tests (user at desktop; app running, ydotool daemon +
socket verified end to end). Meanwhile: mcp-sentinel auditlog export +
remote-server probing, or the offcut selection-stage model decision.

## Blocked
- offcut full-pipeline LLM stage: model capacity on CPU (0.5B schema
  retries exhausted, tinyllama timeout) — unblocked by ROCm Ollama on the
  AMD GPU, or one flash-tier API key for selection only (user decision)
- dissect v0.1.0 tag: GPG signing key fingerprint (user)

## Handoff block (any session)
- State: this table. Read docs/ in each fork repo for per-repo detail.
- Safe to re-run: `python3 scripts/discover.py --json` (beat-list),
  `docker compose ps` (offcut stack up), `mcp-sentinel verify-chain`.
- Do NOT touch: ~/dev/src/github.com/WyattAu/estate.yml without fetch-first
  (concurrent instance active); the nightjar flapped checkout at
  ~/dev/src/github.com/WyattAu/nightjar (use /home/wyatt/builds/nightjar
  for builds — outside the flapping btrfs tree, per fleet rules).
- All four forks: mcp-guard.yml scans PRs — do not remove.

## Log
- 2026-11-02: campaign opened; 4 forks created+seeded; beat-list created
  (registry, rubric, sweep script, MCP threat model); mcp-sentinel v0.1.0
  built+released; sync kit live in cachyos_sys_dotfiles.
- 2026-11-04: offcut full-stack attempt: transcription zero-key PROVEN
  in-container; LLM selection triple-confirmed CPU-bound (runbook); worker
  image rebuilt; port-conflict override shipped.
- 2026-11-03: mcp-guard Action into 4 forks; campaign ledger created;
  mcp-sentinel v0.1.1 (watch daemon, drift detection); nightjar local
  build green (CI-verified + on-box); offcut zero-key transcription E2E
  passed; offcut full-stack attempt triple-confirmed model-capacity finding.
- 2026-11-04/06: nightjar local binary rebuilt post-restarts; M1 smoke
  catalog entries 1-2 resolved; voice tests handed to user.
- 2026-11-01: 4 forks created (nightjar/outrider/offcut/dissect); sync kit
  delivered (opencode V2 config template, skills, audit gates in
  cachyos_sys_dotfiles); fetch-kit 0.2.3 published; offcut whisper default
  flipped; outrider fetcher CI-gated; fleet probes hardened
  (cachyos_sys_dotfiles @ a457572+).
- 2026-10-31: campaign opened (original target sweep); estate.yml healed
  (270 repos green) + audit script bugs fixed; sync kit scoped.
