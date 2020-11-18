from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    WhiskyAPIView,
    WhiskysAPIView,
    AvaliacaoAPIView,
    AvaliacoesAPIView,
    WhiskyViewSet, 
    AvaliacaoViewSet)


router = SimpleRouter()
router.register('whiskys', WhiskyViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('whiskys/', WhiskysAPIView.as_view(), name='whiskys'),
    path('whiskys/<int:pk>/', WhiskyAPIView.as_view(), name='whisky'),
    path('whiskys/<int:whisky_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='whisky_avaliacoes'),
    path('whiskys/<int:whisky_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='whisky_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
