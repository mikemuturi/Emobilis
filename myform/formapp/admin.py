# formapp/admin.py
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'message', 'image')

admin.site.register(Contact, ContactAdmin)
