from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request,'login.html')

def ownerRegister(request):
    return render(request, 'register_owner.html')

def renterRegister(request):
    return render(request, 'register_renter.html')