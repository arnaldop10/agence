from django.urls import path
from .views import index, relatorio_detail_view, grafico_view, pizza_view

urlpatterns = [
    path('', index, name='index'),
    path('relatorio/', relatorio_detail_view, name='relatorio'),
    path('grafico/', grafico_view, name='grafico'),
    path('pizza/', pizza_view, name='pizza'),
]
