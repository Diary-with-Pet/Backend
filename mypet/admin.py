from django.contrib import admin
from mypet.models import MyPet


# Register your models here.
@admin.register(MyPet)
class MyPetAdmin(admin.ModelAdmin):
    list_display = ['user', 'pet_name', 'birthday']
    raw_id_fields = ['user']
