from django.urls import path
from .views import classify_number

urlpatterns = [
    path('api/classify-number/', classify_number, name="classify-number"),
]
