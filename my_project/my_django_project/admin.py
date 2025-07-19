from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'role', 'is_staff' )
    search_fields = ('email', 'name')
    ordering = ('email',)

    fieldsets= (
        (None, {'fields': ('email','name','role', 'password')}),
        ('Permission', {'fields':('is_staff','is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','name', 'role', 'password1', 'password2')
        }),
    )
admin.site.register(User, UserAdmin)    