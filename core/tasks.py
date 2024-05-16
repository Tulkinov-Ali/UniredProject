from celery import shared_task
from datetime import datetime
from django.db import transaction

from core.models import CurrencyExchangeRate


@shared_task
def fetch_and_save_currency_rates():
    import requests
    response = requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/")
    if response.status_code != 200:
        return {'error': 'Failed to fetch data from the API.'}

    exchange_rates = response.json()

    # Fetch all existing exchange rates from the database
    db_exchange_rates = list(CurrencyExchangeRate.objects.values('_id', 'rate'))

    # checking for unique ID, rate change and excluding Nominal from incoming data
    new_exchange_rates = []
    for rate_data in exchange_rates:
        rate_data.pop('Nominal', None)
        obj = {
            '_id': rate_data['id'],
            'rate': float(rate_data['Rate']),
        }
        # changing format of date coming from API inorder to save into a database
        if obj not in db_exchange_rates:
            d = {key.lower(): value for key, value in rate_data.items()}
            d['date'] = datetime.strptime(d['date'], '%d.%m.%Y').date()
            d['_id'] = d.pop('id', None)
            new_exchange_rates.append(CurrencyExchangeRate(**d))

    # Bulk create new exchange rates
    with transaction.atomic():
        CurrencyExchangeRate.objects.bulk_create(new_exchange_rates)

    return {'message': 'Exchange rates saved successfully.'}
