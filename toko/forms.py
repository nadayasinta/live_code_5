from django import forms
from .models import Barang

class Input_Barang(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ('id','nama','harga','deskripsi','gambar')