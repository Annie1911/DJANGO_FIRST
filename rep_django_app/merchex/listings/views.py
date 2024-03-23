from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band,Listings




def band_list(request):
    bands = Band.objects.all()
    return render (request,'listing/band_list.html', {'bands': bands})

def band_detail(request,id):
    bands = Band.objects.get(id=id)
    return render (request,'listing/band_detail.html' , {'band' : bands })




def about(request):
    return HttpResponse('<h1>About us </h1> <p>nous aimons vous rendre service</p')

def listings(request):
    titles = Listings.objects.all()
    return render(request, 'listing/listings.html',{'titres ': titles})


def contact_us(request):
    return HttpResponse('<p>contacter nous </p>')