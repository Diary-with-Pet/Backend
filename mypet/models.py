from django.db import models

from userSystem.models import User


class MyPet(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="mypet", on_delete=models.CASCADE, null=True)
    pet_name = models.CharField(max_length=20)
    birthday = models.CharField(max_length=15)
    gender = models.IntegerField(default=2)
    species = models.CharField(max_length=20)
    profile_image = models.ImageField(default='media/pet/default_image.jpeg', upload_to='pet',
                                      blank=True, null=True)
    profile = models.CharField(max_length=80, blank=True)
