from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html') 

def portfolio(request):
    poj = Project.objects.all()   
    context = {
        "projects":poj
    }
    return render(request,'info-files/projects.html', context)   
