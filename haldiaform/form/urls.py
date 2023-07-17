from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="Home" ),
    path('signup', views.signup, name="Signup" ),
    path('signin', views.signin, name="Signin" ),

]
