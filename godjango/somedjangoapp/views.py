from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. My First View in python MVC Framework.")


def playground(reqeust):
    return HttpResponse('PlayGround Landing Page.')