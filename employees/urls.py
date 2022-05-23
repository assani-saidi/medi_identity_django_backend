from rest_framework import routers, urlpatterns
from .api import EmployeeViewSet

router = routers.DefaultRouter()
router.register("api/employees", EmployeeViewSet, "employees")

urlpatterns = router.urls