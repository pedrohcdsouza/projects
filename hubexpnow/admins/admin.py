from django.contrib import admin
from .models import Client

class ClientsAdmin(admin.ModelAdmin):
    ...

admin.site.register(Client, ClientsAdmin)
