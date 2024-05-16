from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from core.models import CurrencyExchangeRate
from core.serializers import CurrencySerializer


# A view for displaying all currencies from the database and performing currency conversion.
class CurrencyConversionView(GenericAPIView):
    # Filter currencies by date (year, month, day, exact), code, ccy.
    queryset = CurrencyExchangeRate.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['ccynm_en', 'ccynm_uz', 'ccynm_uzc', 'ccynm_ru']
    filterset_fields = {
        'date': ['year', 'month', 'day', 'exact'],
        'code': ['exact'],
        'ccy': ['exact']
    }

    @swagger_auto_schema(
        operation_summary="Retrieve a list of all currencies with optional filtering",
        responses={200: CurrencySerializer(many=True)},
    )
    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = CurrencySerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Convert an amount from Uzbekistan Som (UZS) to the specified currency",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["uzs_amount", "currency_code"],
            properties={
                "uzs_amount": openapi.Schema(type=openapi.TYPE_NUMBER),
                "currency_code": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "converted_amount": openapi.Schema(type=openapi.TYPE_NUMBER),
                    "currency": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
            400: "Currency code and amount must be provided or exchange rate not found for the specified currency code",
        },
    )
    def post(self, request):
        uzs_amount = request.data.get('uzs_amount')
        currency_code = request.data.get('currency_code')

        if uzs_amount is None or currency_code is None:
            return Response({"error": "Currency code and amount must be provided."},
                            status=status.HTTP_400_BAD_REQUEST)

        currency = CurrencyExchangeRate.objects.filter(code=currency_code).first()

        if currency is None:
            return Response({'error': 'Exchange rate not found for the specified currency code.'},
                            status=status.HTTP_400_BAD_REQUEST)

        rate = currency.rate
        converted_amount = uzs_amount / rate
        currency_name = currency.ccy

        return Response({'converted_amount': round(converted_amount, 4), 'currency': currency_name})
