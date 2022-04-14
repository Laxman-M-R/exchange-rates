import datetime
from dateutil import tz

from taskapp.celery import app

@app.task
def create_or_update_exchange_rates_data(exchange_rate_data):
    from .models import Currency, ExchangeRate
    print(exchange_rate_data)
    if exchange_rate_data:
        exchange_rate_date = None
        base_currency = None
        target_currency = None
        exchange_rate = None
        if 'timestamp' in exchange_rate_data and exchange_rate_data['timestamp']:
            exchange_rate_date = (datetime.datetime.fromtimestamp(exchange_rate_data['timestamp'],
                                                                 tz=tz.gettz('Asia/Kolkata')).date())
        if 'base' in exchange_rate_data and exchange_rate_data['base']:
            base_currency, _ = Currency.objects.get_or_create(code= exchange_rate_data['base'])
        if 'rates' in exchange_rate_data and exchange_rate_data['rates']:
            rates = exchange_rate_data['rates']
            for currency, rate in rates.items():
                rate_dict = {}
                target_currency, _ = Currency.objects.get_or_create(code=currency)
                exchange_rate = rate
                if exchange_rate_date and base_currency and target_currency and exchange_rate:
                    rate_dict = {'base_currency': base_currency,
                                 'target_currency': target_currency,
                                 'exchange_rate_date': exchange_rate_date}
                    ExchangeRate.objects.update_or_create(**rate_dict, defaults={"exchange_rate": exchange_rate})