from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Duck
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


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


def delete_duck(request):
    d = Duck.objects.get(id=request.GET['id'])
    d.delete()
    return HttpResponse('duck is removed successfully')


@login_required
def add_to_me(request):
    d = Duck.objects.get(id=request.GET['id'])
    d.owner = request.user
    d.save()
    return HttpResponse('duck is added to the basket')


@login_required
def myducks(request):
    ducks = Duck.objects.filter(owner=request.user)
    return render(request, 'myducks.html', {'myducks': ducks})


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