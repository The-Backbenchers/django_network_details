from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.RoomList.as_view(), name="Home" ),
    
    path('signup', views.signup, name="Signup" ),
    path('login/', auth_views.LoginView.as_view(template_name='signin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('network', views.network_reg, name='network_registration'),
    path('owner', views.owner_reg, name='owner_registration'),
    path('<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
    # path('signin', views.signin, name="Signin" ),
]
