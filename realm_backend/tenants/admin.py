from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'lease_start', 'lease_end', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')
