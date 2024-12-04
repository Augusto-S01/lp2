from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django import forms


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_tenant', 'tenant_name')

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_tenant', 'tenant_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'is_tenant']
    search_fields = ['username', 'email']
    ordering = ['username']


    form = CustomUserChangeForm


    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_tenant', 'tenant_name')}),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_tenant', 'tenant_name')}),
    )


    add_form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
