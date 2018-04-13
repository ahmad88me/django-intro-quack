from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Duck
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'base.html')


def list_ducks(request):
    ducks = Duck.objects.all()
    return render(request, 'duck_list.html', {'ducks': ducks})


def add_duck(request):
    if request.method=="GET":
        return render(request, 'duck_add.html')
    else:
        d = Duck()
        d.model = request.POST['model']
        d.price = float(request.POST['price'])
        d.save()
        return HttpResponse('you duck has been added')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('invalid auth')


def logout_view(request):
    logout(request)
    return HttpResponse('logged out successfully')