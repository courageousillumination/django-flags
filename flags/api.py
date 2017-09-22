"""API for the flags app."""
from rest_framework import viewsets
from rest_framework.response import Response

from flags.utils import get_flag_set


class FlagViewSet(viewsets.ViewSet):
    """A ViewSet for interacting with flags."""

    # The arguments are specified by the ViewSet API.
    # pylint: disable=invalid-name,unused-argument,no-self-use

    def list(self, request):
        """Gets a list of all flags and their values."""
        flag_set = get_flag_set()
        flags = [{'name': x, 'value': flag_set.get_flag_value(x)} for x in flag_set]
        return Response(flags)
