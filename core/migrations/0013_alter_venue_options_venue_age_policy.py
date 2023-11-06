# Generated by Django 4.2.5 on 2023-10-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_event_venue"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="venue",
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="venue",
            name="age_policy",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]