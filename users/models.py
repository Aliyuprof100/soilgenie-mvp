
# Create your models here.

# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model to extend Django's default User."""
    USER_TYPE_CHOICES = (
        ('farmer', 'Farmer'),
        ('agent', 'Agent'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='farmer')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True) # General location for both types

    # Add related_name to avoid clash with auth.User.groups and auth.User.user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="soilgenie_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="soilgenie_user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

class FarmerProfile(models.Model):
    """Additional profile information for Farmers."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='farmer_profile')
    farm_location_detail = models.CharField(max_length=255, blank=True, null=True, help_text="e.g., State, LGA, Village")
    farm_size_hectares = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Farmer Profile for {self.user.username}"

class AgentProfile(models.Model):
    """Additional profile information for Agents."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='agent_profile')
    service_area = models.CharField(max_length=255, blank=True, null=True, help_text="e.g., Kaduna State, Zaria LGA")
    qualification = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Agent Profile for {self.user.username}"

