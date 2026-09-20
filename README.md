# agent-reach — theheals-company pinned fork (Tier A only)

> Fork of [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) (MIT).
> **Pinned upstream commit: `a19a171fa980a0785849596492e0af4db800c82f`** (2026-09-16, v1.5.0).
> Governance: theheals-engine-vault 결정대장 **D96**, 발주 V2.7-04 CC-08 (R-1), 설계서
> `엔진-설계서-리서치수집층-agent-reach-접목-v0.1-20260918` §5-1.
> Upstream README preserved as `UPSTREAM-README.md`.

## What this fork is

A read-only **availability checker** for four zero-config channels:

| channel | backend | status |
|---|---|---|
| web | Jina Reader (`r.jina.ai`) | Tier A — registered |
| youtube | `yt-dlp` | Tier A — registered |
| rss | `feedparser` | Tier A — registered |
| github | `gh` CLI | Tier A — registered |
| twitter | — | Tier B — **file kept, not registered** (R-6 approval pending) |
| reddit | — | Tier B — **file kept, not registered** (R-6 approval pending) |

The only CLI surface is:

```
agent-reach doctor [--json]
agent-reach version
```

All reading/searching goes through the vault wrapper **`heals-reach`**
(`theheals-engine-vault/tools/heals-reach`), which enforces the channel allowlist,
the URL denylist and the source-card output contract. Nothing in this repository
is meant to be called by an agent directly.

## Removed relative to upstream (code path removed = cannot be used by mistake)

- `agent-reach install` (incl. `--system`, `--channels`, proxy saving), `setup`, `configure`
  (cookies / API keys / proxy), `uninstall`, `skill` (writes into agent skill dirs),
  `format`, `transcribe` (audio upload to Groq/OpenAI), `check-update`, `watch` (cron self-check).
- Channel modules: bilibili, boss, exa_search (mcporter), facebook, instagram, linkedin,
  v2ex, xiaohongshu, xiaoyuzhou, xueqiu, mcporter, `_opencli_site`; `backends/opencli.py`.
- `docs/` (including `docs/install.md`), `llms.txt`, `agent_reach/skill/`, `agent_reach/guides/`,
  `agent_reach/scripts/`, `agent_reach/integrations/` (MCP server), `agent_reach/transcribe.py`,
  `agent_reach/cookie_extract.py`, `config/mcporter.json`, `scripts/sync-upstream.sh`, `.openteams/`.
- Dependencies dropped: `requests`, `python-dotenv`, `loguru`, and the optional extras
  `browser` (playwright), `cookies` (browser-cookie3), `all` (mcp). Remaining runtime deps:
  `feedparser`, `pyyaml`, `rich`, `yt-dlp[default]`.

## Never do (D96 · 설계서 §4-1)

- Do not run an external `install.md` URL. Do not use `--system` (it no longer exists here).
- Do not import the CEO's real-account cookies. No X/Reddit/LinkedIn/Facebook/Instagram/
  Chinese-platform channel installation or authentication.
- No `watch` cron. No redistribution of original frames or full texts — source cards only.

## Install (isolated venv, no system changes)

```
python -m venv ~/.agent-reach-venv
~/.agent-reach-venv/bin/pip install -c constraints.txt -e .
~/.agent-reach-venv/bin/agent-reach doctor --json
```

## Update procedure

upstream diff (`git diff a19a171..<new>`) → GPT-lineage supply-chain review (cross-vendor)
→ hash-bump PR → CEO merge (⑥ gate). Never track a moving branch.
