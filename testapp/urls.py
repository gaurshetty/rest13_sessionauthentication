from django.urls import path, include
from .views import EmployeeModelViewsSet, employee_list_api, employee_detail_api
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', EmployeeModelViewsSet, basename='empviewset')

urlpatterns = [
    path('emp/', employee_list_api),
    path('emp/<int:pk>/', employee_detail_api),
    path('', include(router.urls)),
]
