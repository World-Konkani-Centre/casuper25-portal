from os import name
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/<str:camp>', my_register, name='register'),
    path('registered-camps/', camp_registration, name='camp-registration'),
    path('logout/', my_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='authorization/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authorization'
                                                                                        '/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='authorization/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='authorization/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', my_profile, name='profile'),
    path('campers/<str:camp>', members, name='members'),
]
