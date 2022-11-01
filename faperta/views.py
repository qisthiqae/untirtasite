from django.shortcuts import render
from faperta.models import Dosen, Tendik, Mahasiswa
from faperta.forms import FormDosen

# Create your views here.
def isifaperta(request):
    return render (request, 'faperta.html')

def isidatafap(request):
    return render (request, 'datafaperta.html')

def tambah_dosen(request):
    if request.POST:
        form= FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan^^"

            konteks = {
            'form': form,
            'pesan': pesan,
            }

            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)