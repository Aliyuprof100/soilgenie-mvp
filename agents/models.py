from django.db import models

# Create your models here.
# agents/models.py
from django.db import models
from users.models import AgentProfile, FarmerProfile # Import profiles

class Task(models.Model):
    """Represents a task for an agent."""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='tasks')
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='agent_tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task for {self.agent.user.username}: {self.title}"

class Message(models.Model):
    """Represents a message between an agent and a farmer."""
    sender_type_choices = (
        ('agent', 'Agent'),
        ('farmer', 'Farmer'),
    )

    sender_agent = models.ForeignKey(AgentProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    sender_farmer = models.ForeignKey(FarmerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    
    recipient_agent = models.ForeignKey(AgentProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_messages')
    recipient_farmer = models.ForeignKey(FarmerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_messages')

    message_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        sender_name = self.sender_agent.user.username if self.sender_agent else self.sender_farmer.user.username
        recipient_name = self.recipient_agent.user.username if self.recipient_agent else self.recipient_farmer.user.username
        return f"From {sender_name} to {recipient_name} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class Report(models.Model):
    """Represents a field report submitted by an agent."""
    REPORT_TYPES = (
        ('visit', 'Visit Report'),
        ('soil_sample', 'Soil Sample Collection'),
        ('pest_observation', 'Pest Observation Report'),
        ('yield_survey', 'Yield Survey Report'),
        ('other', 'Other'),
    )

    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='reports')
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='reports')
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    report_summary = models.TextField()
    details = models.TextField(blank=True, null=True) # More detailed notes or findings
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.agent.user.username} for {self.farmer.user.username if self.farmer else 'N/A'} - {self.report_type}"

class Appointment(models.Model):
    """Represents a scheduled appointment/visit for an agent with a farmer."""
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='appointments')
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    purpose = models.TextField()
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time'] # Order by upcoming appointments

    def __str__(self):
        return f"Appt: {self.farmer.user.username} with {self.agent.user.username} on {self.appointment_date} at {self.appointment_time}"

