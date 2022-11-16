from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index_view, name='index'),
    path('subscribe/', subscribe_view, name='subscribe')
]
