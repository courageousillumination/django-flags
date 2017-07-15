"""This module contains code for the FlagSet."""
from typing import Any, Dict, List

from flags.flag import Flag


class FlagSet(object):
    """A collection of flags."""

    @classmethod
    def create_from_config(cls, config: List[Dict[str, Any]]) -> 'FlagSet':
        """Creates a FlagSet from a configuration dictionary."""
        return FlagSet([Flag.create_from_config(x) for x in config])

    def __init__(self, flags: List[Flag]) -> None:
        self._flags = {x.name: x for x in flags}

    def get_flag(self, name: str) -> Flag:
        """Get the flag object with the given name."""
        return self._flags[name]
