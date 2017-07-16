"""Overriders for the flags tests."""
from flags.flag_overrider import FlagOverrider


class SimpleOverrider(FlagOverrider):
    """A simple overrider that always return the same value."""

    def __init__(self, value=0):
        self._value = value

    def should_override(self, flag, **kwargs):
        """Yes."""
        return True

    def get_override(self, flag, **kwargs):
        """The answer."""
        return self._value


class NeverOverride(FlagOverrider):
    """An overrider that never applies."""

    def should_override(self, flag, **kwargs):
        return False

    def get_override(self, flag, **kwargs):
        raise NotImplementedError
