from django.db import models
from tenants.models import Tenant

# The UserProfile model extends Django's built-in User with additional fields
# It supports distinguishing landlords, storing contact info, and managing tenants
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Link to Django's User
    phone = models.CharField(max_length=20, blank=True)  # Optional phone number
    address = models.CharField(max_length=255, blank=True)  # Optional address
    is_landlord = models.BooleanField(default=True)  # True if this user is a landlord
    managed_tenants = models.ManyToManyField(Tenant, blank=True, related_name='managers')  # Tenants managed by this user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Display as the username
        return self.user.username
