# Generated by Django 5.0.2 on 2024-03-18 07:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepration_sheet', '0003_prepration_sheet_action_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prepration_sheet',
            name='action',
        ),
        migrations.RemoveField(
            model_name='prepration_sheet',
            name='gfg_link',
        ),
        migrations.RemoveField(
            model_name='prepration_sheet',
            name='leetcode_link',
        ),
        migrations.RemoveField(
            model_name='prepration_sheet',
            name='notes_pdf_link',
        ),
        migrations.RemoveField(
            model_name='prepration_sheet',
            name='youtube_link',
        ),
        migrations.AddField(
            model_name='prepration_sheet',
            name='likes',
            field=models.ManyToManyField(related_name='prgrablog', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prepration_sheet',
            name='slug',
            field=models.SlugField(),
        ),
    ]