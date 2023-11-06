# Generated by Django 4.2.5 on 2023-10-29 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_event_is_cancelled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="venue",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.venue",
            ),
        ),
    ]