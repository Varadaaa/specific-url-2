from virat.views import *
from django.urls import path

app_name = 'anushka'

urlpatterns = [
    path('kholi/', kholi, name='kholi')
]