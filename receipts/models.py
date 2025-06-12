from django.db import models
from financials.models import Transaction

def receipt_upload_to(instance, filename):
    # Use transaction date, tenant name, and original filename for uniqueness
    transaction = instance.transaction
    tenant = transaction.tenant if hasattr(transaction, 'tenant') and transaction.tenant else None
    date_str = transaction.date.strftime('%Y-%m-%d') if hasattr(transaction, 'date') and transaction.date else 'unknown-date'
    tenant_str = f"{tenant.first_name}_{tenant.last_name}" if tenant else 'unknown-tenant'
    ext = filename.split('.')[-1]
    return f"receipts/{date_str}_{tenant_str}_{transaction.id}.{ext}"

class Receipt(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='receipts')
    file = models.FileField(upload_to=receipt_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Receipt for {self.transaction} uploaded at {self.uploaded_at}"
