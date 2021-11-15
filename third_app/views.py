from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index(request: HttpResponse):
    return render(request, "base.html")


def base(request: HttpRequest):
    return render(request, 'body.html')


def image(request: HttpRequest):
    return render(request, 'image.html')


