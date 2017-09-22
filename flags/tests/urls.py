"""URL config for testing."""
from django.conf.urls import include, url
from rest_framework import routers

from flags.api import FlagViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'variables', FlagViewSet, base_name='flags')

# pylint: disable=invalid-name
# yapf: disable
urlpatterns = [
    url(r'^api/', include(ROUTER.urls)),
    ]
