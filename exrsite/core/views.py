from django.shortcuts import render
from django.http import request


# Home view.
def home(request):
    return render(request, 'home.html')


# about view
def about(request):
    return render(request, 'about.html')


# service view
def service(request):
    return render(request, 'service.html')


# service view
def car_insurance(request):
    return render(request, 'car_insurance.html')


# service view
def life_insurance(request):
    return render(request, 'life_insurance.html')


# service view
def health_insurance(request):
    return render(request, 'health_insurance.html')


# service view
def home_insurance(request):
    return render(request, 'home_insurance.html')
