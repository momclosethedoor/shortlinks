from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class CreatedLinksAdmin(admin.ModelAdmin):
    list_display=['id', 'url', 'key']
    
admin.site.register(CreatedLinks, CreatedLinksAdmin)