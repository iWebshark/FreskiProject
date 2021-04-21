from django.urls import path
from catalog import views

app_name = 'catalog_app'

urlpatterns = [
    path('', views.fresco, name='catalog'),
    path('fresco', views.fresco, name='fresco'),
    path('fretwork', views.fretwork, name='fretwork'),
    path('glue', views.glue, name='glue'),
]
