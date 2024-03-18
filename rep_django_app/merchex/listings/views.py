from django.shortcuts import render
from django.http import HttpResponse



def hello(request):
    return HttpResponse('<h1>HELLO WORD </h1>')


def about(request):
    return HttpResponse('<h1>About us </h1> <p>nous aimons vous rendre service</p')

def listings(request):
    return HttpResponse('<ul><li>articles 1</li><li>articles 2</li><li>articles 3</li></ul>')

def contact_us(request):
    return HttpResponse('<p>contacter nous </p>')