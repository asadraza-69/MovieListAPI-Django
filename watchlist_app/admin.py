from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description','active']
    ordering = ['id']

@admin.register(Steamplatform)
class steamplatformAdmin(admin.ModelAdmin):
    list_display = ['id','Plateform', 'about','website']
    ordering = ['id']