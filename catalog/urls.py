from django.urls import path
from catalog import views

app_name = 'catalog_app'

urlpatterns = [
    path('', views.catalog, name='catalog'),
]
