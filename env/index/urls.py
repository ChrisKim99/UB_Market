from django.urls import path
from . import views


urlpatterns = [
    # the first value will be the names of actions
    path('', views.base, name="base"),
    
]