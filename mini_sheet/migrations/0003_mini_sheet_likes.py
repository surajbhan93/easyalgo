# Generated by Django 5.0.2 on 2024-03-18 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_sheet', '0002_mini_sheet_action_mini_sheet_gfg_link_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mini_sheet',
            name='likes',
            field=models.ManyToManyField(related_name='miniblog', to=settings.AUTH_USER_MODEL),
        ),
    ]
