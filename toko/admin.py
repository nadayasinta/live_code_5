from django.contrib import admin
from .models import Barang
# Register your models here.

@admin.register(Barang)
class Ini(admin.ModelAdmin):
    list_display = ('id','nama','harga','deskripsi','gambar')
