from django.urls import path
from Apps.Main.views import login, menu

urlpatterns = [
    path(r'', login),
    path('menu', menu),
]