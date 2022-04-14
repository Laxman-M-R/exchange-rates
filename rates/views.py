from rest_framework.viewsets import ModelViewSet
from django.views.generic.base import TemplateView
from rest_framework import renderers
from rest_framework.response import Response

from .models import ExchangeRate, Currency
from .serializers import ExchangeRateSerializer, CurrencySerializer

class CurrencyModelViewSet(ModelViewSet, TemplateView):
    model = Currency
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

class ExchangeRateModelViewSet(ModelViewSet, TemplateView):
    model = ExchangeRate
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    # template_name = 'rates/index.html'

    #list method example to render both json and html
    # def list(self, request, *args, **kwargs):
    #     response = super(ExchangeRateModelViewSet, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'data': response.data})
    #     return response
