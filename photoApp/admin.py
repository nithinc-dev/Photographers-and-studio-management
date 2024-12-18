from django.contrib import admin

# Register your models here.
from .models import Address, Service, Studio, Photographer , Appointment


admin.site.register(Address)
admin.site.register(Service)
admin.site.register(Studio)
admin.site.register(Photographer)
admin.site.register(Appointment)