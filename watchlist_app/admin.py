from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','active']