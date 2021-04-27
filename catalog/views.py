from django.shortcuts import render
from .models import FrescoProvider, FretworkProvider, GlueProvider


# Create your views here.
def fresco(request):
    fresco_list = FrescoProvider.objects.all()
    return render(request, 'catalog/fresko.html', {'fresco_list': fresco_list})


def fretwork(request):
    fretwork_list = FretworkProvider.objects.all()
    return render(request, 'catalog/fretwork.html', {'fretwork_list': fretwork_list})


def glue(request):
    glue_list = GlueProvider.objects.all()
    return render(request, 'catalog/glue.html', {'glue_list': glue_list})
