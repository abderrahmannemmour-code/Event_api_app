from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact_us import views

router = DefaultRouter()
router.register('', views.ContactUsViewSet, basename='contact-us')

urlpatterns = [
    path('', include(router.urls)),
]
