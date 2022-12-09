from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (("Credenciais", {"fields": ("username", "password")}),)


admin.site.register(User, CustomUserAdmin)
