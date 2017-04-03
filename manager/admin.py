from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token
from .models import Department, Employee

class ManagerAdminSite(AdminSite):
    site_header = 'Employee Manager'
    site_title = 'Employee Manager'
    index_title = 'Administration'

class EmployeeAdmin(ModelAdmin):
    list_display = ('name', 'email', 'department')

def refresh_token(modeladmin, request, queryset):
    for old_token in queryset:
        token_user = old_token.user
        old_token.delete()
        new_token = Token(user=token_user)
        new_token.save()

refresh_token.short_description = 'Refresh selected Tokens'

class ReadOnlyTokenAdmin(TokenAdmin):
    list_display_links = None
    list_display = ('user', 'key', 'created')
    actions = [refresh_token]

admin_site = ManagerAdminSite(name='manageradmin')

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Department)
admin_site.register(Employee, EmployeeAdmin)
admin_site.register(Token, ReadOnlyTokenAdmin)
