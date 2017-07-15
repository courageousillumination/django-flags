"""This module provides the base Flag object."""


class Flag(object):
    """Represents a single configuration flag."""

    @classmethod
    def create_from_config(cls, config: dict) -> 'Flag':
        """Create a new flag from a dictionary config."""
        return Flag(
            name=config['name'],
            flag_type=config['flag_type'],
            default_value=config['default_value'])

    def __init__(self, name, flag_type, default_value):
        self.name = name
        self.flag_type = flag_type
        self.default_value = default_value

    def dostuff(self):
        """docstring."""
        pass
