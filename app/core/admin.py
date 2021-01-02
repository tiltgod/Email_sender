from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = ((None, {'fields': ('email', 'password')}),
                 ('Personal Info', {'fields': ('name', )}),
                 ('Permissions', {'fields': ('is_active', 'is_staff',
                  'is_superuser')}), ('Important dates',
                 {'fields': ('last_login', )}))
    # fieldsets for display in edit page
    add_fieldsets = ((None, {'classes': ('wide', ), 'fields': ('email',
                     'password1', 'password2')}), )
    # add_fieldsets for add test_user_page_change

admin.site.register(models.User, UserAdmin)
