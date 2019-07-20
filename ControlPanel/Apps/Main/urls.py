from django.urls import path
from Apps.Main.views import login, menu
from django.contrib.auth import views

urlpatterns = [
    path(r'', login),
    path('menu', menu),
    path('login/',views.LoginView.as_view(template_name='Main/login.html')),
]