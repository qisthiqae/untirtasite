"""untirtasite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path
from faperta.views import isifaperta
from feb.views import isifeb
from fh.views import isifh
from fisip.views import isifisip
from fkip.views import isifkip
from ft.views import isift
from pascasarjana.views import isipasca
from profil.views import isiprofil
from profil.views import isitentang
from profil.views import isilokasi
from untirtasite.views import isiuntirta
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', isifaperta),
    path('feb/', isifeb),
    path('fh/', isifh),
    path('fisip/', isifisip),
    path('fkip/', isifkip),
    path('ft/', isift),
    path('pascasarjana/', isipasca),
    path('profil/', isiprofil),
    path('tentang/', isitentang),
    path('lokasi/', isilokasi),
    path('untirtasite/', isiuntirta),
    path('', views.isiuntirta),
]
