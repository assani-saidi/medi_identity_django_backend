from django.contrib import admin

from patients.models import Patient

# Register your models here.
# admin.site.register(Patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "id_number", "dob", "address", "contact", "password", "image", "created")
    list_filter = ("name", "surname", "created", "id_number")
    search_fields = ("id_number", "name", "surname", "contact", "address")
    list_display_links = ("name",)
    list_per_page = 10