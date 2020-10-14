from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .User import User


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_company_admin')
    list_filter = ('tags', 'is_staff', 'is_active', 'is_company_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'tags')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_company_admin')}),
    )
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2', 'first_name', 'last_name','tags', 'is_staff', 'is_active',
                'is_company_admin')}
         )
    ]
    search_fields = ('username',)
    ordering = ('username',)




admin.site.register(User, CustomUserAdmin)
