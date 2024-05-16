from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jsonrpcserver import method, Result, Success, Error, dispatch

from core.models import CurrencyExchangeRate
from core.serializers import CurrencySerializer


@method
def ping() -> Result:
    return Success("pong")


# This view is to retrieve a currency list or single currency based on currency code
@method
def currency_list(code=None) -> Result:
    queryset = CurrencyExchangeRate.objects.all()
    if code:
        queryset = queryset.filter(code=code)
    serializer = CurrencySerializer(queryset, many=True)
    return Success(serializer.data)


# This view is to convert uzs amount to specific currency based on its code else convert to all currencies
@method
def exchange(amount, code) -> Result:
    if amount is None or code is None:
        return Error("Currency code and amount must be provided")

    if code:
        try:
            currency = CurrencyExchangeRate.objects.filter(code=code).first()
        except CurrencyExchangeRate.DoesNotExist:
            return Error("Invalid currency code provided")

        rate = currency.rate
        converted_amount = amount / rate
        currency_name = currency.ccy

        return Success({"converted_amount": round(converted_amount, 4), "currency": currency_name})

    currencies = CurrencyExchangeRate.objects.all().values('rate', 'ccy')
    results = []
    for currency in currencies:
        rate = currency['rate']
        currency_name = currency['ccy']
        converted_amount = amount / rate
        results.append({
            "currency": currency_name,
            "converted_amount": round(converted_amount, 4)
        })
    return Success(results)

# This view function serves as an endpoint for JSON-RPC requests.
@csrf_exempt
def jsonrpc_view(request):
    response = dispatch(request.body)
    return JsonResponse(response, safe=False)
