# agents/serializers.py
from rest_framework import serializers
from .models import Task, Message, Report, Appointment
from users.models import AgentProfile, FarmerProfile # Make sure these imports are correct

class TaskSerializer(serializers.ModelSerializer):
    agent_username = serializers.CharField(source='agent.user.username', read_only=True)
    farmer_username = serializers.CharField(source='farmer.user.username', read_only=True)
    
    agent_id = serializers.PrimaryKeyRelatedField(
        queryset=AgentProfile.objects.all(), source='agent', write_only=True
    )
    farmer_id = serializers.PrimaryKeyRelatedField(
        queryset=FarmerProfile.objects.all(), source='farmer', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Task
        fields = (
            'id', 'agent_id', 'agent_username', 'farmer_id', 'farmer_username',
            'title', 'description', 'due_date', 'status', 'date_created', 'last_updated'
        )
        read_only_fields = ('date_created', 'last_updated')

class MessageSerializer(serializers.ModelSerializer):
    sender_agent_username = serializers.CharField(source='sender_agent.user.username', read_only=True)
    sender_farmer_username = serializers.CharField(source='sender_farmer.user.username', read_only=True)
    recipient_agent_username = serializers.CharField(source='recipient_agent.user.username', read_only=True)
    recipient_farmer_username = serializers.CharField(source='recipient_farmer.user.username', read_only=True)

    # Allow setting either agent or farmer as sender/recipient
    sender_agent_id = serializers.PrimaryKeyRelatedField(
        queryset=AgentProfile.objects.all(), source='sender_agent', write_only=True, required=False, allow_null=True
    )
    sender_farmer_id = serializers.PrimaryKeyRelatedField(
        queryset=FarmerProfile.objects.all(), source='sender_farmer', write_only=True, required=False, allow_null=True
    )
    recipient_agent_id = serializers.PrimaryKeyRelatedField(
        queryset=AgentProfile.objects.all(), source='recipient_agent', write_only=True, required=False, allow_null=True
    )
    recipient_farmer_id = serializers.PrimaryKeyRelatedField(
        queryset=FarmerProfile.objects.all(), source='recipient_farmer', write_only=True, required=False, allow_null=True
    )


    class Meta:
        model = Message
        fields = (
            'id', 'sender_agent_id', 'sender_agent_username', 'sender_farmer_id', 'sender_farmer_username',
            'recipient_agent_id', 'recipient_agent_username', 'recipient_farmer_id', 'recipient_farmer_username',
            'message_content', 'timestamp', 'is_read'
        )
        read_only_fields = ('timestamp',)

    def validate(self, data):
        # Ensure only one sender and one recipient type is provided
        if not (data.get('sender_agent') or data.get('sender_farmer')):
            raise serializers.ValidationError("Either sender_agent or sender_farmer must be provided.")
        if data.get('sender_agent') and data.get('sender_farmer'):
            raise serializers.ValidationError("Cannot have both sender_agent and sender_farmer.")
        
        if not (data.get('recipient_agent') or data.get('recipient_farmer')):
            raise serializers.ValidationError("Either recipient_agent or recipient_farmer must be provided.")
        if data.get('recipient_agent') and data.get('recipient_farmer'):
            raise serializers.ValidationError("Cannot have both recipient_agent and recipient_farmer.")

        return data

class ReportSerializer(serializers.ModelSerializer):
    agent_username = serializers.CharField(source='agent.user.username', read_only=True)
    farmer_username = serializers.CharField(source='farmer.user.username', read_only=True)

    agent_id = serializers.PrimaryKeyRelatedField(
        queryset=AgentProfile.objects.all(), source='agent', write_only=True
    )
    farmer_id = serializers.PrimaryKeyRelatedField(
        queryset=FarmerProfile.objects.all(), source='farmer', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Report
        fields = (
            'id', 'agent_id', 'agent_username', 'farmer_id', 'farmer_username',
            'report_type', 'report_summary', 'details', 'date_submitted'
        )
        read_only_fields = ('date_submitted',)

class AppointmentSerializer(serializers.ModelSerializer):
    agent_username = serializers.CharField(source='agent.user.username', read_only=True)
    farmer_username = serializers.CharField(source='farmer.user.username', read_only=True)

    agent_id = serializers.PrimaryKeyRelatedField(
        queryset=AgentProfile.objects.all(), source='agent', write_only=True
    )
    farmer_id = serializers.PrimaryKeyRelatedField(
        queryset=FarmerProfile.objects.all(), source='farmer', write_only=True
    )

    class Meta:
        model = Appointment
        fields = (
            'id', 'agent_id', 'agent_username', 'farmer_id', 'farmer_username',
            'appointment_date', 'appointment_time', 'purpose', 'is_completed', 'date_created'
        )
        read_only_fields = ('date_created',)
