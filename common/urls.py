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
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
