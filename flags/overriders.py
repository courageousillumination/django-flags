"""Some basic overriders for the flags app."""
from typing import Any

from flags.flag import Flag
from flags.flag_overrider import FlagOverrider
from flags.models import SiteFlagOverride


class SiteFlagOverrider(FlagOverrider):
    """An overrider that applies overrides to the whole site."""

    def should_override(self, flag: Flag, **kwargs) -> bool:
        """Whether an override should be considered."""
        return SiteFlagOverride.objects.filter(name=flag.name).exists()

    def get_override(self, flag: Flag, **kwargs) -> Any:
        """Get the override for a specific flag, given a context."""
        return flag.cast_string(SiteFlagOverride.objects.get(name=flag.name).value)
