class FlagOverrider(object):
    """
    A flag overrider is an object that can overide flag values.

    These get various bits of context (request, user, etc.) and use these to determine
    if the flag value should be changed.
    """

    def should_override(self, flag, **kwargs):
        """Whether an override should be considered."""
        return False

    def get_override(self, flag, **kwargs):
        """Get the override for a specific flag, given a context."""
        raise NotImplementedError
