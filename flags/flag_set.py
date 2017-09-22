"""This module contains code for the FlagSet."""
from typing import Any, Dict, Iterable, List

from flags.flag import Flag
from flags.flag_overrider import FlagOverrider


class FlagSet(Iterable):
    """A collection of flags."""

    @classmethod
    def create_from_config(cls, config: List[Dict[str, Any]],
                           overriders: List[FlagOverrider]=None) -> 'FlagSet':  # pylint:disable=bad-whitespace,line-too-long
        """Creates a FlagSet from a configuration dictionary."""
        return FlagSet([Flag.create_from_config(x) for x in config], overriders)

    def __init__(self, flags: List[Flag], overriders: List[FlagOverrider]) -> None:
        self._flags = {x.name: x for x in flags}
        self._overriders = overriders if overriders else []

    def get_flag(self, name: str) -> Flag:
        """Get the flag object with the given name."""
        return self._flags[name]

    def get_flag_value(self, name: str, **kwargs) -> Any:
        """Get a flag value, with all overriders."""
        flag = self.get_flag(name)
        for overrider in self._overriders:
            if overrider.should_override(flag, **kwargs):
                return overrider.get_override(flag, **kwargs)
        return flag.default_value

    def __iter__(self):
        """Iterate over all flag names."""
        for flag_name in self._flags:
            yield flag_name
