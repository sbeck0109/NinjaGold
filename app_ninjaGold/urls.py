from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('process_money', views.process_money, name='my_process'),
  path('reset', views.reset, name='my_reset'),
  path('starting', views.starting, name='my_starting'),
]
