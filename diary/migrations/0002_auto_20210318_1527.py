# Generated by Django 3.1.4 on 2021-03-18 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diaryimage',
            old_name='image',
            new_name='images_set',
        ),
    ]
