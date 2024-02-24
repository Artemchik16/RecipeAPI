from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    change_user_password_template = None
    fieldsets = (
        (
            None,
            {"fields": ("phone_number", "email", "username")},
        ),
        (
            _("Base info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = (
        'id',
        'full_name',
        'username',
        'phone_number',
    )
