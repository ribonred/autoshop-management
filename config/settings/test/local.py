from config.settings.local import *  # noqa

LOGGING["loggers"].update(
    {
        "test": {
            "handlers": ["console",],
            "level": "DEBUG",
            "propagate": False,
        }
    }
)
