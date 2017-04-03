from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import Employee

class EmployeeAdminSite(AdminSite):
    site_header = 'Employee Manager'

class EmployeeAdmin(ModelAdmin):
    list_display = ('name', 'email', 'department')

admin_site = EmployeeAdminSite(name='employeeadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Employee, EmployeeAdmin)
