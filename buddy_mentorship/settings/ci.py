from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "buddy_mentorship",
        "USER": "buddy_mentorship",
        "HOST": "postgres",
        "PASSWORD": "postgres",
    }
}

CHROME_HEADLESS = True
CHROME_SANDBOX = False
