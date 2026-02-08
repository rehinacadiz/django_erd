from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, ProjectViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
