from rest_framework import routers, urlpatterns
from .api import ProviderViewSet

router = routers.DefaultRouter()
router.register("api/providers", ProviderViewSet, "providers")

urlpatterns = router.urls