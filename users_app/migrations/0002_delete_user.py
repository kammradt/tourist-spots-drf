# Generated by Django 2.2.3 on 2019-07-22 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]