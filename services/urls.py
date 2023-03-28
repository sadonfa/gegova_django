from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.services, name="services")
]