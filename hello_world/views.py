from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if (request.POST):
        return HttpResponse("You must haved POSTed something")
    else:
        return  HttpResponse(request.method) 