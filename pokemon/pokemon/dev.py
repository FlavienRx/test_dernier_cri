import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .settings import *

# Django Debug Toolbar Settings
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configuring-internal-ips

INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]
