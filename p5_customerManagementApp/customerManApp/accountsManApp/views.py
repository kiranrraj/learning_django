from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accountsManApp/home.html')

def products(request):
    return render(request, 'accountsManApp/products.html')

def customer(request):
    return render(request, 'accountsManApp/profile.html')