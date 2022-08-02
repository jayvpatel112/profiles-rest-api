from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.Helloviewset, basename='hello-viewset')

urlpatterns = [
    path('get', views.helloapi),
    path('post', views.posthelloapi),
    path('update-patch', views.helloapi),
    path('', include(router.urls))
]
