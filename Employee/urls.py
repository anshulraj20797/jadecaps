from django.urls import path, include
from Employee import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employee', views.EmployeeViewSet,)


urlpatterns = [
    path('',include(router.urls)),
    path('employee50/', views.Employee50API.as_view(), name='emp50'),
    path('company/', views.CompanyList.as_view(), name='company'),
    path('company/<int:pk>', views.CompanyDetails.as_view(), name='company-detail'),
    
]
