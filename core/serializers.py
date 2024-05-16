from rest_framework import serializers

from core.models import CurrencyExchangeRate


# Serializer for CurrencyExchangeRate model
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchangeRate
        fields = ['_id', 'code', 'ccy', 'ccynm_en', 'ccynm_uz', 'ccynm_uzc', 'ccynm_ru', 'rate', 'diff', 'date']
