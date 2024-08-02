from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def aboutusPage(requests):
    return HttpResponse("About Us Page Refactory")
