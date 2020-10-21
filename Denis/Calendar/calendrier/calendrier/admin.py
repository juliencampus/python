from django.contrib import admin
from .models import Types, Horaires, Rdv

# Register your models here.
admin.site.register(Types)
admin.site.register(Horaires)
admin.site.register(Rdv)