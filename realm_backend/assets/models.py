from django.db import models

class Asset(models.Model):
    APPLIANCE_TYPES = [
        ("fridge", "Fridge"),
        ("oven", "Oven"),
        ("washer", "Washer"),
        ("dryer", "Dryer"),
        ("hvac", "HVAC"),
        ("water_heater", "Water Heater"),
        ("dishwasher", "Dishwasher"),
        ("other", "Other"),
    ]
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=100, choices=APPLIANCE_TYPES)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    age_years = models.PositiveIntegerField(null=True, blank=True, help_text="Age of the appliance in years")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_name_display()} ({self.brand} {self.model}) for {self.property}"
