"""The base FlagOverrider class."""
from typing import Any

from flags.flag import Flag


class FlagOverrider(object):  # pragma: no cover
    """
    A flag overrider is an object that can overide flag values.

    These get various bits of context (request, user, etc.) and use these to determine
    if the flag value should be changed.
    """

    # pylint: disable=unused-argument,no-self-use

    def should_override(self, flag: Flag, **kwargs) -> bool:
        """Whether an override should be considered."""
        return False

    def get_override(self, flag: Flag, **kwargs) -> Any:
        """Get the override for a specific flag, given a context."""
        raise NotImplementedError
