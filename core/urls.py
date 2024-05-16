from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator

from core.views import CurrencyConversionView
from core.service.stats import rate_chart
from core.rpc import jsonrpc_view

schema_view = get_schema_view(
    openapi.Info(
        title="Currency Exchange API",
        default_version="v1",
        description="API for currency exchange rates and conversion",
    ),
    public=True,
    generator_class=OpenAPISchemaGenerator,
)

urlpatterns = [
    path('currencies/', CurrencyConversionView.as_view(), name='home'),
    path('rate-chart/', rate_chart, name='rate_chart'),
    path('rpc/', jsonrpc_view),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
