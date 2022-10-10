from django.shortcuts import render

# Create your views here.
def isifaperta(request):
    return render (request, 'faperta.html')