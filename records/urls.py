from rest_framework import routers, urlpatterns
from .api import RecordViewSet

router = routers.DefaultRouter()
router.register("api/records", RecordViewSet, "records")

urlpatterns = router.urls