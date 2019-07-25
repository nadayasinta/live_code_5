from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.PositiveIntegerField()
    deskripsi = models.TextField()
    gambar = models.URLField()