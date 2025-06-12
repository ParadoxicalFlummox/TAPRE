from django.db import models
from tenants.models import Tenant

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_landlord = models.BooleanField(default=True)
    managed_tenants = models.ManyToManyField(Tenant, blank=True, related_name='managers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
