from django.urls import path
from . import views


urlpatterns = [
    path('inicio/<nombre>', views.hola, name='inicio'),
]

