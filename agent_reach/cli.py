# -*- coding: utf-8 -*-
"""Agent Reach CLI — theheals-company pinned fork (Tier A only).

Usage:
    agent-reach doctor [--json]     # read-only availability check of Tier A channels
    agent-reach version

Removed relative to upstream a19a171fa980a0785849596492e0af4db800c82f (see README.md):
install (including ``--system``), setup, configure (cookies/keys/proxy), uninstall,
skill (writes into agent skill dirs), format, transcribe (Groq/OpenAI upload),
check-update and watch (scheduled self-update).  This fork never installs system
packages, never reads browser cookies, never uploads media, and never writes outside
its own config directory.  Reading/searching is done by the vault wrapper
``heals-reach`` (theheals-engine-vault/tools/heals-reach), never by this CLI.
"""

import argparse
import json
import os
import sys

from agent_reach import __version__


def _ensure_utf8_console():
    """Best-effort Windows console UTF-8 setup for CLI runtime only."""
    if sys.platform != "win32":
        return
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return
    try:
        import io
        if hasattr(sys.stdout, "buffer"):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "buffer"):
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    _ensure_utf8_console()

    parser = argparse.ArgumentParser(
        prog="agent-reach",
        description=(
            "Agent Reach — theheals pinned fork. Tier A channels only "
            "(web, youtube, rss, github). Read-only health check; no installer."
        ),
    )
    parser.add_argument("--version", action="version", version=f"Agent Reach v{__version__}")
    sub = parser.add_subparsers(dest="command", help="Available commands")

    p_doctor = sub.add_parser("doctor", help="Check Tier A channel availability (read-only)")
    p_doctor.add_argument("--json", action="store_true",
                          help="Output machine-readable JSON instead of the text report")

    sub.add_parser("version", help="Show version")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "version":
        print(f"Agent Reach v{__version__} (theheals pinned fork, upstream a19a171)")
        sys.exit(0)

    if args.command == "doctor":
        _cmd_doctor(args)


def _cmd_doctor(args=None):
    from agent_reach.config import Config
    from agent_reach.doctor import check_all, format_report

    config = Config(read_only=True)
    results = check_all(config)

    if args is not None and getattr(args, "json", False):
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    report = format_report(results)
    try:
        from rich import print as rich_print
    except ImportError:
        print(report)
    else:
        rich_print(report)


if __name__ == "__main__":
    main()
