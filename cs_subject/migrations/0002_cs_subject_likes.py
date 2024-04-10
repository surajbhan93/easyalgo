# Generated by Django 5.0.2 on 2024-03-18 08:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs_subject', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cs_subject',
            name='likes',
            field=models.ManyToManyField(related_name='csblog', to=settings.AUTH_USER_MODEL),
        ),
    ]