# calculator/urls.py

from django.urls import path
from .views import calculator

urlpatterns = [
    path('', calculator, name='calculator'),  # The root URL for the calculator app
]