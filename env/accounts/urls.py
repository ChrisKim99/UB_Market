from django.urls import path
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    # the first value will be the names of actions
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]