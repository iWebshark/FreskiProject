from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from .models import Example, ExampleImage, Contact


# Create your views here.
def index(request):
    exampls = list(Example.objects.all()[:4])
    return render(request, 'common/index.html', {'examples': exampls})


def about(request):
    return render(request, 'common/about.html')


def contacts(request):
    return render(request, 'common/contacts.html')


def examples(request):
    exampls = list(Example.objects.all())
    return render(request, 'common/examples.html', {'examples': exampls})


def examples_get(request, id_to_get: int):
    example = Example.objects.get(pk=id_to_get)
    objects_img = list(ExampleImage.objects.filter(example=example))

    img_dict = dict()
    img_dict[str(example.default_image)] = str(example.default_image)
    for img in objects_img:
        img_dict[str(img.image)] = str(img.image)

    return HttpResponse(json.dumps(img_dict), content_type='application/json')
