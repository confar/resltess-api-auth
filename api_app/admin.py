from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django import forms

# Register your models here.
from .models import ApiUser



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'type','is_admin')
    list_filter = ('is_admin',)
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('type',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(ApiUser, UserAdmin)
admin.site.unregister(Group)
