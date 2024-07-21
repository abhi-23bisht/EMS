from django.contrib import admin
from ems.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','id','department')

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)