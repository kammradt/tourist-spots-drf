# Generated by Django 2.2.3 on 2019-07-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0002_auto_20190715_1934'),
        ('attractions_app', '0001_initial'),
        ('comments_app', '0002_auto_20190715_1934'),
        ('tourist_spots_app', '0008_auto_20190715_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristspots',
            name='attractions',
        ),
        migrations.AddField(
            model_name='touristspots',
            name='attractions',
            field=models.ManyToManyField(blank=True, to='attractions_app.Attraction'),
        ),
        migrations.RemoveField(
            model_name='touristspots',
            name='comments',
        ),
        migrations.AddField(
            model_name='touristspots',
            name='comments',
            field=models.ManyToManyField(blank=True, to='comments_app.Comment'),
        ),
        migrations.RemoveField(
            model_name='touristspots',
            name='reviews',
        ),
        migrations.AddField(
            model_name='touristspots',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='reviews_app.Review'),
        ),
    ]