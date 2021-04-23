from django.shortcuts import render
from .models import Example, Contact


# Create your views here.
def index(request):
    exampls = list(Example.objects.all()[:4])
    return render(request, 'common/index.html', {'examples': exampls})


def about(request):
    return render(request, 'common/about.html')


def contacts(request):
    return render(request, 'common/contacts.html')


def examples(request):
    return render(request, 'common/examples.html')
