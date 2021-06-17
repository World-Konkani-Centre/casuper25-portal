from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('camp/', camp, name='camp'),
    path('teams/<str:camp>', website, name='team-website'),
    path('events/<str:camp>', submit, name='submit'),
    path('camp/<str:camp>', camp_home, name='camp-home'),
    path('camp-register', camp_register, name='camp-register'),
    path('schedule/<str:camp>', schedule, name='schedule'), 

]