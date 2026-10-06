from django.urls import path
from .views import pierwszy_endpoint

urlpatterns = [
    path('pierwszy/', pierwszy_endpoint),
]