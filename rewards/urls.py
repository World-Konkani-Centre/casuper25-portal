from django.urls import path

from .views import *

urlpatterns = [
    path('award/',give_award , name='give_award'),
    path('award-list/<str:camp>', award_list, name='award-list'),
    path('leaderboard/<str:camp>', leaderboard,name="leaderboard"),
]
