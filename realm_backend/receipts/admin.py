from .models import Receipt
from django.contrib import admin

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'uploaded_at', 'description')
    search_fields = ('description',)
