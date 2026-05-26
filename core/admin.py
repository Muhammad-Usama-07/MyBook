from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin display for our User model.
    Extends Django's built-in UserAdmin which already has:
    - Password change forms
    - Permission management
    - Group management
    """

    # Columns shown in the user list page
    list_display = [
        'username', 'email',
        'first_name', 'last_name',
        'role', 'is_active', 'date_joined'
    ]

    # Filters in the right sidebar of admin
    list_filter = ['role', 'is_active', 'is_staff']

    # Searchable fields
    search_fields = ['username', 'email', 'first_name', 'last_name']

    # Add 'role' field to the user edit form in admin
    fieldsets = UserAdmin.fieldsets + (
        ('MyBook Role', {'fields': ('role', 'profile_picture')}),
    )

    # Add 'role' field to the user creation form in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('MyBook Role', {'fields': ('role',)}),
    )