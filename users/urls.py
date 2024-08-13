from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,user_list
from django.contrib.auth import views as auth_views
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/', user_list, name='user-list'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]