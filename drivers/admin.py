from django.contrib import admin
from .models import Driver,Car,Path,Location

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Path)
admin.site.register(Location)