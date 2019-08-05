from rest_framework import routers
from django.conf.urls import url, include
from employee.views import EmployeeViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    url('employee/', include(router.urls)),
]