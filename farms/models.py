# farms/models.py
from django.db import models
from users.models import FarmerProfile # Import the FarmerProfile model from your users app
# import json # No longer explicitly needed for JSONField handling

class Farmland(models.Model):
    """
    Represents a specific farmland area mapped by a farmer or agent.
    Linked to a FarmerProfile.
    """
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE, # If a FarmerProfile is deleted, all their farmlands are deleted too
        related_name='farmlands', # Allows you to access farmer.farmlands.all()
        help_text="The farmer profile this farmland belongs to."
    )
    farm_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional name for the farm, e.g., 'Main Maize Field'."
    )
    location_detail = models.CharField(
        max_length=255,
        help_text="Detailed location of the farm (e.g., State, LGA, Village)."
    )
    area_hectares = models.FloatField(
        help_text="Calculated area of the farm in hectares."
    )
    intended_crop_type = models.CharField(
        max_length=100,
        help_text="The type of crop intended to be grown on this farmland."
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional notes or specific details about the farmland."
    )
    # Store GeoJSON data as a JSONField. This is the correct way to store JSON objects.
    geojson_data = models.JSONField( # <--- CRITICAL CHANGE HERE
        blank=True,
        null=True,
        help_text="GeoJSON representation of the farm's boundary or point."
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the farmland record was added."
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text="The last date and time the farmland record was updated."
    )

    class Meta:
        verbose_name = "Farmland"
        verbose_name_plural = "Farmlands"
        ordering = ['date_added'] # Order farmlands by when they were added

    def __str__(self):
        # Human-readable representation of the Farmland object
        return (f"{self.farm_name if self.farm_name else 'Unnamed Farm'} "
                f"({self.intended_crop_type} - {self.area_hectares:.2f} ha) "
                f"by {self.farmer.user.username}")