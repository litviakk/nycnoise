# Generated by Django 4.2.5 on 2023-10-02 18:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=tinymce.models.HTMLField(max_length=100),
        ),
    ]
