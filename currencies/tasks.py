import requests
from celery import shared_task
from django.conf import settings
from currencies.models import Currency


@shared_task
def update_exchange_rates():
    api_url = f'http://api.exchangeratesapi.io/v1/latest'
    resp = requests.get(api_url, params={'access_key': settings.EXCHANGE_RATES_API_KEY})
    if resp.status_code == 200:
        json_response = resp.json()
        available_currencies = Currency.available_currencies()
        for curr in available_currencies:
            print(f"Updating {curr}")
            if curr in json_response['rates'].keys():
                Currency.objects.filter(code=curr).update(
                    conversion_rate=float(1 / json_response['rates'][curr])
                )
