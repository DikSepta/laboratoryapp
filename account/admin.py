from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

from account.models import Account
from account.forms import UserChangeForm, UserCreationForm

# Register your models here.
class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The forms to add and change user instances    
    list_display = ('email', 'date_of_birth', 'first_name', 'last_name','phone','address', 'is_staff','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Personal info', {'fields': ('date_of_birth','address', 'phone')}),
        ('Permissions', {'fields': ('is_admin','is_staff', 'is_superuser')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'address', 'phone', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Account, MyUserAdmin)
admin.site.unregister(Group)

