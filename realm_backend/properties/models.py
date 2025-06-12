from django.db import models

# The Property model stores information about a real estate property owned or managed by the landlord
class Property(models.Model):
    # Address fields for the property
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='USA')
    # Construction and inspection dates
    construction_date = models.DateField(null=True, blank=True)
    last_inspection_date = models.DateField(null=True, blank=True)
    # Optional description and timestamps
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Display the property as its address
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
