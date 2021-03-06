from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
# Create your views here.


def home(request):
    return render(request, 'todo\home.html')


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mytodos')
            except IntegrityError:
                return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': 'Username already taken'})
        else:
            return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': "Password did not match"})
            # return render(request, 'todo/signup.html')


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def mytodos(request):
    return render(request, 'todo/mytodos.html')
