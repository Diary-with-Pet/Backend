# Generated by Django 3.1.4 on 2021-03-18 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20210318_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diaryimage',
            old_name='images_set',
            new_name='image',
        ),
    ]
