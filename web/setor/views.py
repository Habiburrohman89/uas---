from django.shortcuts import render

from .models import setorTunai,tarikTunai

def tor(request):
    tah = setorTunai.objects.all()

    context = {
        'tah': tah,
    }
    return render(request,'setor.html',context)

def tar(request):
    tuh = tarikTunai.objects.all()

    context = {
        'tuh': tuh,
    }
    return render(request,'tarik.html',context)