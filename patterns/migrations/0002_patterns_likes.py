# Generated by Django 5.0.2 on 2024-03-18 08:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patterns', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patterns',
            name='likes',
            field=models.ManyToManyField(related_name='pattblog', to=settings.AUTH_USER_MODEL),
        ),
    ]
