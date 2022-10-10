from django.shortcuts import render
from django.template import loader

def isiuntirta(request):
    return render (request, 'index.html')