# Generated by Django 4.2.8 on 2023-12-06 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0046_alter_datemessage_message_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="staticpage",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
    ]
