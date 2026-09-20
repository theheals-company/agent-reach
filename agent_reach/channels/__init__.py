# -*- coding: utf-8 -*-
"""
Channel registry — theheals pinned fork.

Only Tier A channels are registered (V2.7-04 CC-08 R-1, decision D96):
web · youtube · rss · github.

Tier B channel modules (twitter.py, reddit.py) are kept in the tree for the
future R-6 approval but are deliberately NOT registered here, so `doctor`
never probes them and the vault wrapper's allowlist cannot reach them.
Every other upstream channel file was deleted (code path removed).
"""

from typing import List, Optional

from .base import Channel
from .github import GitHubChannel
from .rss import RSSChannel
from .web import WebChannel
from .youtube import YouTubeChannel

ALL_CHANNELS: List[Channel] = [
    GitHubChannel(),
    YouTubeChannel(),
    RSSChannel(),
    WebChannel(),
]

#: Tier B modules present on disk but outside the allowlist (not registered).
TIER_B_UNREGISTERED = ("twitter", "reddit")


def get_channel(name: str) -> Optional[Channel]:
    """Get a registered (Tier A) channel by name."""
    for ch in ALL_CHANNELS:
        if ch.name == name:
            return ch
    return None


def get_all_channels() -> List[Channel]:
    """Get all registered (Tier A) channels."""
    return ALL_CHANNELS


__all__ = [
    "Channel",
    "ALL_CHANNELS",
    "TIER_B_UNREGISTERED",
    "get_channel",
    "get_all_channels",
]
