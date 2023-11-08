from .base import *  # noqa

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")  # noqa
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

