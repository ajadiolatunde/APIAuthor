from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.
def authorlist(request,id):
    print ("---------",id)
    return  HttpResponse("Cool")

def login_view(request):

    print ("Re-----------",request.POST.lists())
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        print ('succesful-------',token.__dict__)
        d = {'status':'success'}
        return HttpResponse(token.key,status=240)
    else:
        print ('failed-------')
        d = {'status':'failed'}
        return HttpResponse("Failed",status=230)

