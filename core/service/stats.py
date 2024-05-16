from django.shortcuts import render

from core.models import CurrencyExchangeRate


# a function to retrieve chart of specific currency
def rate_chart(request):
    # Retrieve all available currencies

    currencies = [
        "USD", "EUR", "RUB", "GBP", "JPY", "AZN", "BDT", "BGN", "BHD", "BND",
        "BRL", "BYN", "CAD", "CHF", "CNY", "CUP", "CZK", "DKK", "DZD", "EGP",
        "AFN", "ARS", "GEL", "HKD", "HUF", "IDR", "ILS", "INR", "IQD", "IRR",
        "ISK", "JOD", "AUD", "KGS", "KHR", "KRW", "KWD", "KZT", "LAK", "LBP",
        "LYD", "MAD", "MDL", "MMK", "MNT", "MXN", "MYR", "NOK", "NZD", "OMR",
        "PHP", "PKR", "PLN", "QAR", "RON", "RSD", "AMD", "SAR", "SDG", "SEK",
        "SGD", "SYP", "THB", "TJS", "TMT", "TND", "TRY", "UAH", "AED", "UYU",
        "VES", "VND", "XDR", "YER", "ZAR"
    ]

    selected_currency = request.GET.get('currency', 'USD')

    # Retrieve exchange rate data for the selected currency
    currency_rates = CurrencyExchangeRate.objects.filter(ccy=selected_currency).order_by('date')

    # Extract dates and rates
    dates = [rate.date.strftime('%Y-%m-%d') for rate in currency_rates]
    rates = [rate.rate for rate in currency_rates]

    context = {
        'currencies': currencies,
        'selected_currency': selected_currency,
        'dates': dates,
        'rates': rates,
    }
    return render(request, 'rate_chart.html', context)
