from django.urls import path
from . import views


urlpatterns = [
    # the first value will be the names of actions
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile")
    
]