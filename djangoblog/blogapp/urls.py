from django.shortcuts import render
from django.http import response


def home(request):
    return HttpResponse("this my blog")