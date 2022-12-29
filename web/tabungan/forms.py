from django.forms import ModelForm
from django import forms
from .models import gadai

class formgadai(ModelForm):
    class Meta:
        model = gadai
        fields = '__all__'


        widgets = {
            'Nama' : forms.TextInput({'class':'form-control'}),
            'Nik' : forms.TextInput({'class':'form-control'}),
            'Alamat' : forms.TextInput({'class':'form-control'}),
            'Jumlah_Pinjaman' : forms.TextInput({'class':'form-control'}),
            'Barang_Jaminan' : forms.TextInput({'class':'form-control'}),
            'Bunga_Per_Th ' : forms.TextInput({'class':'form-control'}),
            'Biaya_administrasi' : forms.TextInput({'class':'form-control'}),
        }


        