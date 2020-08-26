from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def base(request):
# request has the value passed from clients
# as specified in the seetings of main, the function will render pages from the templates
# can return some value {"name": "value to return"}
    return render(request, 'main/base.html')
