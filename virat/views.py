from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kholi(request):
    return HttpResponse('<h1><marquee>50th centurey in WC </marquee></h1>')
    