from django.shortcuts import render, redirect
from .models import Barang
from .forms import Input_Barang


# Create your views here.
def home(request):
    list_barang=Barang.objects.all()
    return render (request, 'home.html',{'list_barang':list_barang})
    # return render(request,'home.html',{}) 

def barang_detail(request,barang_id):
    try:
        barang = Barang.objects.get(pk=barang_id)
    except Blog.DoesNotExist:
        raise Http404("Barang does not exist")
    return render(request, 'barang_detail.html', {'barang':barang})

def barang_tambah(request):
    if request.method == 'POST':
        form = Input_Barang(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('halaman_home')
    else:
        form = Input_Barang()
    return render(request, 'barang_tambah.html',{'form':form})