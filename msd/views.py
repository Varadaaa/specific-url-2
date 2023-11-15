from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('<h1><marquee>Best Of All</marquee></h1>')