from django.shortcuts import render


# Create your views here.
def fresco(request):
    return render(request, 'catalog/fresko.html')


def fretwork(request):
    return render(request, 'catalog/fretwork.html')


def glue(request):
    return render(request, 'catalog/glue.html')
