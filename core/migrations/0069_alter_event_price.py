# Generated by Django 4.2.10 on 2024-08-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_event_user_submission_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(blank=True, choices=[('🌀 free', '🌀 free'), ('🌀 notaflof', '🌀 notaflof'), ('$', '$'), ('$$', '$$ ($30+)'), ('$$$', '$$$ ($50+)'), ('$$$$', '$$$$ ($75+ lol y)')], max_length=255, null=True),
        ),
    ]