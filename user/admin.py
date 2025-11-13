# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User


# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     # Fields shown in the user list
#     list_display = ("username", "email", "role", "is_staff", "is_active")
#     list_filter = ("role", "is_staff", "is_active")

#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         ("Personal Information", {"fields": ("first_name", "last_name", "email")}),
#         ("Role & Permissions", {"fields": ("role", "is_staff", "is_superuser", "is_active")}),
#         ("Important Dates", {"fields": ("last_login", "date_joined")}),
#     )

#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("username", "email", "password1", "password2", "role", "is_staff", "is_active"),
#         }),
#     )

#     search_fields = ("username", "email")
#     ordering = ("id",)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User Admin with role support"""

    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Role & Permissions", {"fields": ("role", "is_staff", "is_superuser", "is_active")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "role", "is_staff", "is_active"),
        }),
    )

