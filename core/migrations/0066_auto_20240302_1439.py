# Generated by Django 4.2.10 on 2024-03-02 19:39

from django.db import migrations


def change_venue_field_closed_to_open(apps, schema_editor):
    Venue = apps.get_model("core", "Venue")

    # save into venue's new is_open field from closed (flipping the bit)
    for venue in Venue.objects.all():
        venue.is_open = not venue.closed
        venue.save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0065_alleventproxy_venue_is_open"),
    ]

    operations = [
        migrations.RunPython(change_venue_field_closed_to_open),
    ]
