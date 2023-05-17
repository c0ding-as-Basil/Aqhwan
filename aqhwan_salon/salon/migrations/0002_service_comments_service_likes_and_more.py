# Generated by Django 4.2 on 2023-05-15 11:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='comments',
            field=models.ManyToManyField(related_name='commented_services', through='salon.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='likes',
            field=models.ManyToManyField(related_name='liked_services', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(upload_to='service_pictures'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
