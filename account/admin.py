from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Links


class ProfileInlineContent(admin.StackedInline):
    model = Profile


class LinksInlineContent(admin.StackedInline):
    model = Links


class CustomUserAdmin(UserAdmin):
    model = User
    inlines = [ProfileInlineContent, LinksInlineContent]
    list_display = ('username', 'email', 'last_login', 'is_active')
    list_display_links = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal', {'fields': ('email', 'first_name','last_name','profile_picture')}), # noqa
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','user_permissions')}), # noqa
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')} # noqa
        ), # noqa
    )

    search_fields = ('username',)
    ordering = ('username',)

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['is_staff'].disabled = True
            form.base_fields['is_active'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True

        return form


admin.site.register(User, CustomUserAdmin)
