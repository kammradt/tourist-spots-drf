# Generated by Django 2.2.3 on 2019-07-16 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0002_auto_20190715_1934'),
        ('attractions_app', '0001_initial'),
        ('addresses_app', '0001_initial'),
        ('comments_app', '0002_auto_20190715_1934'),
        ('tourist_spots_app', '0011_auto_20190715_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=False)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses_app.Address')),
                ('attractions', models.ManyToManyField(blank=True, to='attractions_app.Attraction')),
                ('comments', models.ManyToManyField(blank=True, to='comments_app.Comment')),
                ('reviews', models.ManyToManyField(blank=True, to='reviews_app.Review')),
            ],
        ),
        migrations.DeleteModel(
            name='TouristSpots',
        ),
    ]