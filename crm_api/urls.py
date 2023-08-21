from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')  # Use CustomerViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
