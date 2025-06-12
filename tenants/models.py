from django.db import models

# Create your models here.
class Tenant(models.Model):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    DEPENDANT = 'dependant'
    TENANT_TYPE_CHOICES = [
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
        (DEPENDANT, 'Dependant'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    current_address = models.CharField(max_length=255, blank=True)
    lease_start = models.DateField(null=True, blank=True)
    lease_end = models.DateField(null=True, blank=True)
    tenant_type = models.CharField(max_length=20, choices=TENANT_TYPE_CHOICES, default=PRIMARY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_tenant_type_display()})"
