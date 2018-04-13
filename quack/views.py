from django.shortcuts import render
from django.http import HttpResponse
from models import Duck


def home(request):
    return render(request, 'base.html')


def list_ducks(request):
    ducks = Duck.objects.all()
    return render(request, 'duck_list.html')