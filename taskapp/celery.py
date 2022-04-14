from __future__ import absolute_import
import os
from django.apps import AppConfig, apps
from django.conf import settings
from django.core.mail import send_mail
from celery import Celery
from celery.utils.log import get_task_logger
from celery.signals import task_failure, task_prerun, task_revoked, task_success

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exchange_rates.config.settings")
app = Celery('exchange_rates.taskapp')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)
print(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # pragma: no cover

@app.task
def add(x, y):
    logger.info("Adding {0} + {1}".format(x, y))
    return x + y

@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)

def check_celery_status():
    status = False
    try:
        app.connection().connect()
        workers = app.control.ping(timeout=0.1)
        if workers:
            status = True
    except:
        pass

    return status
