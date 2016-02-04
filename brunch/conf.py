from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

settings.BRUNCH_CMD = getattr(settings, 'BRUNCH_CMD', ("/usr/bin/env", "brunch"))
settings.BRUNCH_SHELL = getattr(settings, 'BRUNCH_SHELL', False)
settings.BRUNCH_SERVER = getattr(settings, 'BRUNCH_SERVER', False)

if not hasattr(settings, 'BRUNCH_DIR'):
    raise ImproperlyConfigured("You must specify an absolute path for BRUNCH_DIR")
