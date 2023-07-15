
from django.urls import path
from . import views


urlpatterns = [
    path('Home', views.home, name="Home" ),
]