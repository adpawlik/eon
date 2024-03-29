# Generated by Django 3.1.6 on 2021-02-17 17:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('old_price', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('parking_places', models.IntegerField(default=0)),
                ('sqm', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='offer.category')),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dealer.dealer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('offer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='offer_images', to='offer.offer')),
            ],
        ),
    ]
