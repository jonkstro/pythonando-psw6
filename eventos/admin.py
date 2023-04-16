from django.contrib import admin

from eventos.models import Evento, Certificado

# Register your models here.
admin.site.register(Evento)
admin.site.register(Certificado)