from django.forms import ModelForm
from django import forms
from faperta.models import Dosen

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        exclude= ['Photo']

        widgets= {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'Tanggallahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Alamatrumah' : forms.TextInput({'class':'form-control'}),
        }