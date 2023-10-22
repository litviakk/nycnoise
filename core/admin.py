from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Event, Venue

admin.site.site_title = "nyc noise"
admin.site.site_header = "nyc noise"


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "venue", "starttime", "get_description_as_text")

    def get_description_as_text(self, obj):
        return mark_safe(obj.description)

    get_description_as_text.short_description = "Description"


admin.site.register(Event, EventAdmin)


class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "age_policy", "neighborhood_and_borough")
    search_fields = ("name",)


admin.site.register(Venue, VenueAdmin)
