from django.urls import re_path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'exchange_rates', views.ExchangeRateModelViewSet, basename="exchange_rates")
router.register(r'currencies', views.CurrencyModelViewSet, basename="currencies")


urlpatterns = router.urls

