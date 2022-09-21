#from django.http import HttpResponse
from django.shortcuts import render


def recife(request):
    return render(request, 'home.html')
