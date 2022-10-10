from django.shortcuts import render

# Create your views here.
def isiprofil(request):
    return render (request, 'profil.html')
def isitentang(request):
    return render(request,'tentang.html')
def isilokasi(request):
    return render(request,'lokasi.html')