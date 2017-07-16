"""Basic models that are included with the flags app."""
from django.db import models


class SiteFlagOverride(models.Model):
    """A site wide flag override."""
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
