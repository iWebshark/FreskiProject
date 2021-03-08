from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def about(request):
    return render(request, 'common/about.html')


def contacts(request):
    return render(request, 'common/contacts.html')


def examples(request):
    return render(request, 'common/examples.html')