from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "employment_number", "name", "surname","password", "company", "created")
    list_filter = ("employment_number", "name", "surname", "company", "created")
    search_fields = ("employment_number", "name", "surname", "company", "created")
    list_display_links = ("name",)
    list_per_page = 10