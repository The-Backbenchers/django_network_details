from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home" ),
    path('signin', views.signin, name="signin" ),
]
