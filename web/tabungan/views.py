from django.shortcuts import render
from .forms import formgadai

def gad(request):
    hab = formgadai()

    context = {
        'hab': hab,
    }
    return render(request,'tabungan.html',context)

