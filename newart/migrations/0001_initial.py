# Generated by Django 5.0.3 on 2024-04-13 16:57

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='static/images/newart')),
                ('text', tinymce.models.HTMLField()),
                ('date', models.DateTimeField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(to='newart.cat_news')),
            ],
        ),
    ]
