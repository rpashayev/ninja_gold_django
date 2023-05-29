from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.start_page),
    path('start', views.start),
    path('game', views.index),
    path('process', views.process_money),
    path('reset', views.clear),
]

