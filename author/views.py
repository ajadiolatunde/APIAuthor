from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def authorlist(request,id):
    print ("---------",id)
    return  HttpResponse("Cool")
