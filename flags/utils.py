"""
Utility functions for interacting with the flags app.

Most people will want to only use the get_flag_value, but the others are exposed just in case.
"""
import json
from typing import IO, List

from django.conf import settings
from django.utils.module_loading import import_string

from flags.flag_overrider import FlagOverrider
from flags.flag_set import FlagSet


def get_overriders() -> List[FlagOverrider]:
    """Get the active overriders."""
    if hasattr(settings, 'FLAGS_OVERRIDERS'):
        return [import_string(x)() for x in settings.FLAGS_OVERRIDERS]
    return []


def load_flag_set(fin: IO) -> FlagSet:
    """Load a flag set from a files stream."""
    return FlagSet.create_from_config(json.load(fin), get_overriders())


def load_flag_set_path(path: str) -> FlagSet:
    """Load a flag set based on the path."""
    return load_flag_set(open(path))


def get_flag_set() -> FlagSet:
    """Get the currently configured FlagSet."""
    return load_flag_set_path(settings.FLAGS_CONFIG_FILE)


def get_flag_value(name, **kwargs):
    """Get the value of a flag."""
    return get_flag_set().get_flag_value(name, **kwargs)
