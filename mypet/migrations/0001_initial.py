# Generated by Django 3.1.4 on 2021-03-11 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=15)),
                ('gender', models.IntegerField(default=2)),
                ('species', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, default='media/pet/default_image.jpeg', null=True, upload_to='pet')),
                ('profile', models.CharField(blank=True, max_length=80)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mypet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
