from django.contrib import admin
from taggit.models import TaggedItem, Tag
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .User import User


class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class CustomUserAdmin(MyModelAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'tag_list', 'is_staff', 'is_active', 'is_company_admin')
    list_filter = ('tags', 'is_staff', 'is_active', 'is_company_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_company_admin')}),
        ('Tags', {'classes': ('',), 'fields': ('tags',)})
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
