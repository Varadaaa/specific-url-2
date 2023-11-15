from msd.views import *
from django.urls import path

app_name ='worldcup'

urlpatterns= [
    path('dhoni/', dhoni, name='dhoni'),
    
]