# Generated by Django 4.1.3 on 2022-11-16 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribedusers',
            name='city',
        ),
    ]
