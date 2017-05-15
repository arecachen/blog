from django.shortcuts import render
from django.template.context_processors import request
import datetime

#from django.http import HttpResponse 

# Create your views here.

def main(request):
    content={'like':'Django 很棒','range100': range(100)}

    return render(request,'main/main.html',content)

def about(request):
    content={'dt':datetime.datetime.now()}
    return render(request,'main/about.html',content)