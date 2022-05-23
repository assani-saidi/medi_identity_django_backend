from django.conf.urls import url
from rest_framework_swagger import get_swagger_view

schema_view = get_swagger_view(title='Medi-Identity-API')

urlpatterns = [
    url(r'^$', schema_view)
]