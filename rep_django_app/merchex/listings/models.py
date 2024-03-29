from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# listings/models.py

class Band(models.Model):

     


    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices =Genre.choices, max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)



    def __str__(self):
        return self.name 



class Listings(models.Model):

    class Type(models.TextChoices):
        Records ='Rd'
        Clothing ='Cl' 
        Posters ='Post'
        Miscellaneous ='M'

        
    title = models.fields.CharField(max_length=100)
    describe = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(validators=[MinValueValidator(2001),MaxValueValidator(2024)])
    type = models.fields.CharField( choices =Type.choices ,max_length=50)
    band = models.ForeignKey(Band, null=True,  on_delete = models.SET_NULL)

    def __str__(self):
        return self.title
