from django.shortcuts import render
# Create your views here.
# Note: The stuff above this will already be in this file.
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')