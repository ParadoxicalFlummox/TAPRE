from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'zip_code', 'country', 'construction_date', 'last_inspection_date', 'created_at', 'updated_at')
    search_fields = ('address', 'city', 'state', 'zip_code')
