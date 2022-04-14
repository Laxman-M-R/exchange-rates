# python django imports
from django.dispatch import receiver
from django.db import transaction
from taskapp.celery import check_celery_status
from rates.tasks import create_or_update_exchange_rates_data

def exchange_rates_signal(data_dict, **kwargs):
    exchange_rates_data = data_dict.get("exchange_rates_data", {})
    celery_status = check_celery_status()
    if celery_status:
        transaction.on_commit(lambda: create_or_update_exchange_rates_data.delay(exchange_rates_data))
    else:
        print("Celery not running. So unable to create or update Exchange Rates Data.")

