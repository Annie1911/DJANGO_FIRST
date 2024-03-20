from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band,Listings




def hello(request):
    bands = Band.objects.all()
    return render (request,'listing/hello.html', {'bands': bands})



def about(request):
    return HttpResponse('<h1>About us </h1> <p>nous aimons vous rendre service</p')

def listings(request):
    titles = Listings.objects.all()
    return render(request, 'listing/listings.html',{'titres ': titles})


def contact_us(request):
    return HttpResponse('<p>contacter nous </p>')