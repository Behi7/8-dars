from django.contrib import admin
from . import models
from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     model = models.User
#     list_display = ["username", "email"]
#     fieldsets = [(None, {'fields': ('username', 'password')}),
#                  ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#                  ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#                  ('Important dates', {'fields': ('last_login', 'date_joined', 'img', 'bio')}),
#                 ]    


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(models.Blog)
admin.site.register(models.BlogImg)
admin.site.register(models.BlogVideo)
admin.site.register(models.Comment)
