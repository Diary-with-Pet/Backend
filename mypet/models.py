from django.db import models

from userSystem.models import User


class MyPet(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="mypet", on_delete=models.CASCADE, null=True)
    pet_name = models.CharField(max_length=20)
    gender = models.IntegerField(default=2)
    species = models.CharField(max_length=20)
    species_detail = models.CharField(max_length=45)
    profile = models.CharField(max_length=50)
