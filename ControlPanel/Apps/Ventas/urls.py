from django.urls import path
from Apps.Ventas.views import 

urlpatterns = [
    path(r'', index),
    path('view/', view),
]