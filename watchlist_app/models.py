from django.db import models

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
    active = models.BooleanField(verbose_name="active",default=True, null= True ,blank= True)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = u'movie'
    