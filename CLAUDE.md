# CLAUDE.md — theheals pinned fork of agent-reach

- This repository is a **read-only availability checker** (`agent-reach doctor`). It has no
  installer, no cookie import, no transcription, no self-update. Do not re-add them.
- Agents never call `agent-reach` directly. Use the vault wrapper `heals-reach`
  (theheals-engine-vault `tools/heals-reach`, skill `.claude/skills/heals-reach/SKILL.md`).
- Registered channels are exactly `web · youtube · rss · github` (`agent_reach/channels/__init__.py`).
  `twitter.py` / `reddit.py` stay unregistered until decision R-6.
- Upstream pin: `a19a171fa980a0785849596492e0af4db800c82f`. Any bump goes through
  diff → cross-vendor supply-chain review → PR → CEO merge. See README.md.
- Channel contract (unchanged from upstream): `can_handle(url)`, `check(config) -> (status, message)`,
  set `active_backend`; really probe the backend, `shutil.which` alone is not proof.
