from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def  home(request):
    # return HttpResponse("Hello My Mariya")
    return  render(request,'generator/home.html',{'password':'wgrehkhRKke'})
# Create your views here.
def  about(request):
    # return HttpResponse("Hello My Mariya")
    return  render(request,'generator/about.html')
def  password(request):
    # return HttpResponse("<h1>eggs are so tasty</h1>")

    characters= list('eihwgjrajkohhOaej')
    # length=10
    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMOPQRSTUVWXYZ")
    if request.GET.get('special'):
        characters.extend("@#$%^&*!?")
    if request.GET.get('numbers'):
        characters.extend("0123456789")
    le= int(request.GET.get('length',4))
    thepassword = ''
    for x in range(le):
        thepassword += random.choice(characters)
    return  render(request,'generator/password.html',{'password':thepassword})