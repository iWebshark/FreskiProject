from django.conf.urls.static import static
from django.urls import path

from FreskiProject import settings
from common import views

app_name = 'common_app'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('about', views.about, name='about'),
                  path('contacts', views.contacts, name='contacts'),
                  path('examples', views.examples, name='examples'),
                  path('examples/get/<int:id_to_get>', views.examples_get, name='examples_get'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
