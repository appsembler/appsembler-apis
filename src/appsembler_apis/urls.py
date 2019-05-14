from django.conf.urls import include, url
from rest_framework import routers

from appsembler_apis import views

router = routers.DefaultRouter()


# Add your endpoints. Example:

# router.register(
#     r'insert-api-endpoint',
#     views.SiteDailyMetricsViewSet,
#     base_name='insert-api-endpoint-base-name')


urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
]
