from ..base import *

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

SITE_ID = 3

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

SERVER_EMAIL = "server@crate.io"
DEFAULT_FROM_EMAIL = "support@crate.io"
CONTACT_EMAIL = "support@crate.io"

# MIDDLEWARE_CLASSES += ["privatebeta.middleware.PrivateBetaMiddleware"]

PACKAGE_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
PACKAGE_FILE_STORAGE_OPTIONS = {
    "bucket": "crate-production",
    "custom_domain": "packages.crate.io",
}

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
# STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"

AWS_STORAGE_BUCKET_NAME = "crate-media-production"
AWS_S3_CUSTOM_DOMAIN = "media.crate.io"

# PRIVATE_BETA_ALLOWED_URLS = [
#     "/account/login/",
#     "/account/signup/",
#     "/account/confirm_email/",
# ]

# PRIVATE_BETA_ALLOWED_HOSTS = [
#     "simple.crate.io",
# ]

INTERCOM_APP_ID = "79qt2qu3"
