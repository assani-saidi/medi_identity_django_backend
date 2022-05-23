from django.contrib import admin

from providers.models import Provider

# Register your models here.
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "contact")
    list_filter = ("id", "name", "address", "contact")
    search_fields = ("name", "address", "contact")
    list_display_links = ("name",)
    list_per_page = 10