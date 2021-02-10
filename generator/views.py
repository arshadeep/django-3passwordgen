from django.shortcuts import render#render helps us to pass back a template
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html')#the dictionary gets pass forward to my home.html
#we cant just reeturn back string we have to format it as http response
# Create your views here.
#first flow goes from urls.py to home method above then to home.html where user enters length and taps button then it goes to urls and comes to view.py now to password method
def password(request):#data from the form gets supplied here,all variables are contained in the request variable
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length=int(request.GET.get('length',12))#12 is deafault value
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')