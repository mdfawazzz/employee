from django.contrib import admin
from .models import *
# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display=('id','name','department','dob','designation','salary','address','others')

admin.site.register(Data,DataAdmin)