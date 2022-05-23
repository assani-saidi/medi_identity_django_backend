from django.contrib import admin

from conditions.models import Condition

# Register your models here.
# admin.site.register(Patient) 
@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ("illness", "treatment", "diagnosed")
    list_filter = ("illness", "treatment", "diagnosed")
    search_fields = ("illness", "diagnosed")
    list_display_links = ("illness",)
    list_per_page = 10