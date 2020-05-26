from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'pwr_generator/home.html')

def password(request):


    thepass = ''
    chrs = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chrs.extend(list('ABCDEFGHJIKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chrs.extend(list('@£$!&'))

    if request.GET.get('special'):
        chrs.extend(list('123456789'))

    for i in range(length):
        thepass += random.choice(chrs)

    return render(request, 'pwr_generator/password.html',{'password':thepass})

def about(request):

    return render(request,'pwr_generator/about.html' )
