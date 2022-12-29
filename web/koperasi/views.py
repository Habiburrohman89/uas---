from django.shortcuts import render
from .models import tabungan

def kop(request):
    bog = tabungan.objects.all()

    context = {
        'bog': bog,
    }
    return render(request, 'koperasi.html',context)
