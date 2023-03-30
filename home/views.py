from django.shortcuts import render

def home(request):
    return render(request, 'home.html')    

def sigup(request):
    return render(request, 'sigup.html')    
