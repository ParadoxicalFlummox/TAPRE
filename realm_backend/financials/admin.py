from .models import Account, Category, Transaction
from django.contrib import admin

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_income')
    verbose_name_plural = 'Categories'

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'category', 'amount', 'transaction_type', 'date', 'created_at')
