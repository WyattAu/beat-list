# beat-list

Standing registry of competitive targets: viral/trending repositories and
critical infrastructure gaps worth beating with the WyattAu estate.

Maintained per the fleet coordination rules (2026-11-01): fetch before
writes, push immediately, canon manifest is engineering-standards/estate.yml.

## Sources

- GitHub trending snapshots (githot.dev, gitstock.org, githubtrending.today)
- Hacker News front page + Show HN (news.ycombinator.com/front)
- Incident advisories: GitHub Advisory DB, Pillar/CloudSEK/OX research blogs
- Weekly digests (tommyz.blog, startupcorners devtools digest)

## Cadence

Weekly sweep; each sweep appends candidates to `registry/` with a score.
Anything scoring ≥ 12/15 gets a ROADMAP pitch; anything flagged
`infra-critical` jumps the queue.

## Scoring rubric (15 points)

| Criterion | Pts | Question |
|---|---|---|
| Estate leverage | 5 | Do estate crates/skills give an unfair build advantage? |
| Wedge clarity | 4 | Can we name the differentiator in one sentence? |
| Upstream gap | 3 | Is the incumbent weak on trust/reliability/honesty? |
| Demand signal | 2 | Trending stars, incident frequency, HN traction |
| Maintenance cost | 1 (inverse) | Is staying green cheap for us? |
