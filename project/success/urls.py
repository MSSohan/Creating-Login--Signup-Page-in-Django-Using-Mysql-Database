from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('success/', views.tokenaction, name='success'),
]