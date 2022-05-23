from django.contrib import admin

from records.models import Record

# Register your models here.
# admin.site.register(Patient)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "treatment", "dieses", "authorised_by", "created")
    list_filter = ("patient", "treatment", "dieses", "authorised_by", "created")
    search_fields = ("patient", "treatment", "dieses", "authorised_by", "created")
    list_display_links = ("patient",)
    list_per_page = 10