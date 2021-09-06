'''
Urls for shortener app urlshortener/urls.py
'''

from django.urls import path
from .views import home_view, redirect_url_view

appname = "shortener"

urlpatterns = [
    # Home view
    path('', home_view, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]