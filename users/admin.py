from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_landlord', 'created_at', 'updated_at')
    search_fields = ('user__username', 'phone', 'address')
