from django.contrib import admin

from .models import Event, Venue

admin.site.site_title = "nyc noise"
admin.site.site_header = "nyc noise"

admin.site.register(Event)
admin.site.register(Venue)
