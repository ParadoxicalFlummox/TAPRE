from django.db import models

# The Tenant model represents a person renting a property
# It supports primary, secondary, and dependant tenants, and stores contact and lease info
class Tenant(models.Model):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    DEPENDANT = 'dependant'
    TENANT_TYPE_CHOICES = [
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
        (DEPENDANT, 'Dependant'),
    ]
    # Basic personal and contact info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    current_address = models.CharField(max_length=255, blank=True)
    # Lease information
    lease_start = models.DateField(null=True, blank=True)
    lease_end = models.DateField(null=True, blank=True)
    # Tenant type (primary, secondary, dependant)
    tenant_type = models.CharField(max_length=20, choices=TENANT_TYPE_CHOICES, default=PRIMARY)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Display tenant as 'First Last (Type)'
        return f"{self.first_name} {self.last_name} ({self.get_tenant_type_display()})"
