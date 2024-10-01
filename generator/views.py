from django.shortcuts import render
import random
import datetime


def home(request):
    return render(request, 'generator/home.html')
 

def about(request):
    y = datetime.datetime.now()
    return render(request, 'generator/about.html', {'year': y.year})


def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')


    chars = list('abcdefghijklmnopqrstvuwxyz')
    if uppercase:
        chars.extend('ABCDEFGHIJKLMNOPQRSTVUWXYZ')
    if numbers:
        chars.extend('1234567890')
    if symbols:
        chars.extend('!@#$%^&*()_+=><')


    thepass = ''
    for i in range(length):
        thepass+=random.choice(chars)

      

    return render(request, 'generator/password.html', {'password': thepass} )