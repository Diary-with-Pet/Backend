# Generated by Django 3.1.4 on 2021-03-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20210318_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryimage',
            name='image',
            field=models.ImageField(blank=True, default='http://172.0.0.1:8000/media/diary/default_image.jpeg', null=True, upload_to='diary'),
        ),
    ]