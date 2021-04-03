from django.contrib import admin

from userSystem.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
