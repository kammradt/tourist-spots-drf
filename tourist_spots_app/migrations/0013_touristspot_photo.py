# Generated by Django 2.2.3 on 2019-07-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_spots_app', '0012_auto_20190716_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tourist_spots_images'),
        ),
    ]
