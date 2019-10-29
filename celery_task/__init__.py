from celery import Celery
from django.conf import settings
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proj.settings")
app = Celery()
app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

