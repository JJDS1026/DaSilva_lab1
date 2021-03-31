# home/urls.py
from django.urls import path

from .views import index, index_card_view, profile_view, key_view, this_week_view, today_view

urlpatterns = [
    path('', index, name='index'),
    path('index_card', index_card_view, name='index_card'),
    path('profile', profile_view, name='profile_view'),
    path('key', key_view, name='key_view'),
    path('this_week', this_week_view, name='this_week_view'),
    path('today', today_view, name='today_view'),
]
