from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.


class Steamplatform(models.Model):
    Plateform = models.CharField(verbose_name="Plateform", max_length=50, null= True ,blank= True)
    about = models.CharField(verbose_name="about",max_length=200, null= True ,blank= True)
    website = models.URLField(verbose_name="website",max_length= 150)
    
    def __str__(self):
        return self.Plateform
    
    def __unicode__(self):
        return '%s' % self.Plateform

    class Meta:
        db_table = u'steamplatform' 

class Movie(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, null= True ,blank= True) 
    description = models.CharField(verbose_name="description",max_length=200, null= True ,blank= True)
    plateform = models.ForeignKey(Steamplatform,on_delete = models.CASCADE,verbose_name="plateform", null= True ,blank= True,related_name = "plateform_name")
    active = models.BooleanField(verbose_name="active",default=True, null= True ,blank= True)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = u'movie'

class Review(models.Model):
    rating = models.PositiveIntegerField(verbose_name="rating",validators = [MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(verbose_name="description",max_length=100, null= True ,blank= True)
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE,verbose_name = "movie", null= True, blank= True, related_name= "review_movie")    
    active = models.BooleanField(verbose_name="active",default=True, null= True ,blank= True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.rating)
    class Meta:
        db_table = u'review'