from django.urls import path
from .views import static_view

urlpatterns = [
    path('static_part/<int:pk>/', static_view, name="static_url")
]
