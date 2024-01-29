from django.urls import path

from ads.apps import AdsConfig
from ads.views import AdCreateAPIView, AdListAPIView, AdAllListAPIView, AdRetrieveAPIView, AdUpdateAPIView, \
    AdDestroyAPIView

app_name = AdsConfig.name

urlpatterns = [
    # URLs Ad:
    path('create/', AdCreateAPIView.as_view(), name='ads_create'),
    path('', AdListAPIView.as_view(), name='ads_list'),  # Список объявлений текущего пользователя.
    path('public/', AdAllListAPIView.as_view(), name='ads_public_list'),  # Список всех объявлений.
    path('<int:pk>/', AdRetrieveAPIView.as_view(), name='ads_get'),
    path('update/<int:pk>/', AdUpdateAPIView.as_view(), name='ads_update'),
    path('delete/<int:pk>/', AdDestroyAPIView.as_view(), name='ads_delete'),
]
