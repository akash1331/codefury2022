# Generated by Django 3.0.8 on 2022-08-13 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furyapp', '0005_auto_20220814_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup_post',
            name='media_files',
        ),
    ]
