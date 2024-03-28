from django import forms
from listings.models import Band

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
         #exclude = ('active', 'official_homepage')  # ajoutez cette ligne

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100 , required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000 )