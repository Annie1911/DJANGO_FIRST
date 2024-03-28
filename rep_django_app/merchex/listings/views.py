from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail  import send_mail
from listings.models import Band,Listings
from .form import ContactForm,BandForm




def band_list(request):
    bands = Band.objects.all()
    listings = Listings.objects.all()
    return render (request,'listing/band_list.html', {'bands': bands,'listings': listings})

def band_detail(request,id):
    bands = Band.objects.get(id=id)
    return render (request,'listing/band_detail.html' , {'band' : bands })
def listings(request):
    # bands = Band.objects.all()
    listings = Listings.objects.all()
    # return render (request,'listing/listings.html', {'bands': bands,'listings': listings})
    return render (request,'listing/listings.html', {'listings': listings})


def band_create(request):

    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,'listing/band_create.html',
            {'forms': form})


def band_change(request,id):
    band = Band.objects.get(id=id)
    form = BandForm(request.POST)
    if form.is_valid():
        # créer une nouvelle « Band » et la sauvegarder dans la db
        form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
        return redirect('band-detail', band.id)

    else:

        form = BandForm(instance = band)
    return render(request, 'listing/band_change.html', {'form': form, 'band': band})


def band_delete(request, id):
    bands = Band.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('bands-list')

    return render(request, 'listing/band_delete.html', { 'bands': bands})







def contact_us(request):

    if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
    else:
 # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactForm()

    return render(request,'listing/contact.html',{'form': form})




def about(request):
    return HttpResponse('<h1>About us </h1> <p>nous aimons vous rendre service</p>')
