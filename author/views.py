from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from author.ses import Ses
from rest_framework.decorators import api_view
import json


# Create your views here.
def authorlist(request,id):
    print ("session-1----",request.session.__dict__)

    print ("---------",id)
    return  HttpResponse("Cool")

def login_view(request):

    print ("session-2----",request.session.__dict__)

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

@api_view(['GET'])
def get_session(request):
    print ("all re--------------",request.META['HTTP_AUTHENTICATION'])
    ses = Session.objects.all()
    print ("sesion-all",ses)
    myses = Ses(request)
    print ("tunde ----op-------",myses.__dict__)
    res = {}
    res['message'] = "Got data"
    res['session'] = myses.__dict__['session']


    return  Response(res)

@api_view(["GET"])
def token(request):

    token, _ = Token.objects.get_or_create(user_id=1)
    return Response({"token": token.key})




