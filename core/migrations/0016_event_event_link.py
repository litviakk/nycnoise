# Generated by Django 4.2.5 on 2023-10-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_venue_google_maps_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_link",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]