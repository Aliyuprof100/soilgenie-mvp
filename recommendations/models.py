# Create your models here.
# recommendations/models.py
from django.db import models
from farms.models import Farmland # Import Farmland from the farms app

class Recommendation(models.Model):
    """Stores AI-generated recommendations for a specific farmland."""
    RECOMMENDATION_TYPES = (
        ('fertilizer', 'Fertilizer Application'),
        ('irrigation', 'Irrigation Advice'),
        ('pest_disease', 'Pest & Disease Warning'),
        ('yield_forecast', 'Yield Forecast Update'),
        ('soil_health', 'Soil Health Advice'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending Review'),
        ('issued', 'Issued to Farmer'),
        ('completed', 'Completed by Farmer'),
        ('archived', 'Archived'),
    )

    farmland = models.ForeignKey(Farmland, on_delete=models.CASCADE, related_name='recommendations')
    recommendation_type = models.CharField(max_length=50, choices=RECOMMENDATION_TYPES)
    recommendation_text = models.TextField()
    date_issued = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    agent_notes = models.TextField(blank=True, null=True, help_text="Agent's notes on issuing/following up.")

    def __str__(self):
        return f"Rec: {self.farmland.intended_crop_type} - {self.recommendation_type} ({self.farmland.farmer.user.username})"

