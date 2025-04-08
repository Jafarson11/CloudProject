# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Registration URL placed first to take precedence
    path('register/', RegisterView.as_view(), name='auth_register'),
    
    # Then include the router's URLs
    path('', include(router.urls)),
]
