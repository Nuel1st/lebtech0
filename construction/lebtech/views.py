from django.shortcuts import render

# Create your views here.

def home(request):
    return render( request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def project(request):
    return render(request, 'project.html')

def team(request):
    return render(request, 'team.html')

