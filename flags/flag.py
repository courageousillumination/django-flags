"""This module provides the base Flag object."""
from enum import Enum
from typing import Any


class FlagType(Enum):
    """Enum for various flag types."""
    INT = 1


class Flag(object):
    """Represents a single configuration flag."""

    @classmethod
    def create_from_config(cls, config: dict) -> 'Flag':
        """Create a new flag from a dictionary config."""
        return Flag(
            name=config['name'],
            flag_type=config['flag_type'],
            default_value=config['default_value'])

    def __init__(self, name: str, flag_type: str, default_value) -> None:
        self.name = name
        self.flag_type = FlagType[flag_type.upper()]
        self.default_value = default_value

    def cast_string(self, string: str) -> Any:
        """Cast a string into the appropriate type for this flag."""
        if self.flag_type == FlagType.INT:
            return int(string)
        raise ValueError('Flag encountered unknown type {}'.format(self.flag_type))
