from django.db import models
from realm_backend.financials.models import Transaction

def receipt_upload_to(instance, filename):
    # Custom file naming: receipts/YYYY-MM-DD_First_Last_transactionID.ext
    transaction = instance.transaction
    tenant = transaction.tenant if hasattr(transaction, 'tenant') and transaction.tenant else None
    date_str = transaction.date.strftime('%Y-%m-%d') if hasattr(transaction, 'date') and transaction.date else 'unknown-date'
    tenant_str = f"{tenant.first_name}_{tenant.last_name}" if tenant else 'unknown-tenant'
    ext = filename.split('.')[-1]
    return f"receipts/{date_str}_{tenant_str}_{transaction.id}.{ext}"

# The Receipt model stores uploaded files (images, PDFs, etc.) for proof of transactions
# Each receipt is linked to a Transaction and uses a custom file naming scheme
class Receipt(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='receipts')  # Link to the related transaction
    file = models.FileField(upload_to=receipt_upload_to)  # File upload (image, PDF, etc.)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for upload
    description = models.TextField(blank=True)  # Optional description

    def __str__(self):
        # Display as 'Receipt for <transaction> uploaded at <date>'
        return f"Receipt for {self.transaction} uploaded at {self.uploaded_at}"
