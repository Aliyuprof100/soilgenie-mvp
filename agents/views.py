from django.shortcuts import render

# Create your views here.
# agents/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, Message, Report, Appointment
from .serializers import TaskSerializer, MessageSerializer, ReportSerializer, AppointmentSerializer
# from rest_framework.permissions import IsAuthenticated # Uncomment when auth is ready
from users.models import AgentProfile, FarmerProfile # Import FarmerProfile for relationship
from django.db.models import Q # Import Q for complex lookups in MessageListCreateView

class TaskListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating tasks."""
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter tasks for the logged-in agent (if authentication is enabled)
        # For demonstration purposes, this currently returns all tasks.
        # Once authentication is fully set up, you would uncomment the following lines
        # and modify them to filter by the authenticated agent's profile:
        # if self.request.user.is_authenticated and self.request.user.user_type == 'agent':
        #     try:
        #         agent_profile = AgentProfile.objects.get(user=self.request.user)
        #         return Task.objects.filter(agent=agent_profile).order_by('due_date')
        #     except AgentProfile.DoesNotExist:
        #         return Task.objects.none() # Agent profile not found
        return Task.objects.all().order_by('due_date')

    def perform_create(self, serializer):
        # Associate the task with the requesting agent (if authentication is enabled)
        # For demonstration purposes, this currently saves without strict agent linkage.
        # Once authentication is set up, you would uncomment/modify:
        # if self.request.user.is_authenticated and self.request.user.user_type == 'agent':
        #     try:
        #         agent_profile = AgentProfile.objects.get(user=self.request.user)
        #         serializer.save(agent=agent_profile)
        #     except AgentProfile.DoesNotExist:
        #         raise serializers.ValidationError("Agent profile not found for the current user.")
        # else:
        serializer.save() # For demo, save directly if no agent context


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a specific task."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated] # Ensure only owner/assigned agent can modify

class MessageListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating messages."""
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter messages relevant to the logged-in user (agent or farmer)
        # For demonstration, this returns all messages.
        # Once authentication is set up, filter by the current user's messages:
        # user = self.request.user
        # if user.is_authenticated:
        #     if user.user_type == 'agent':
        #         return Message.objects.filter(
        #             Q(sender_agent__user=user) | Q(recipient_agent__user=user)
        #         ).order_by('-timestamp')
        #     elif user.user_type == 'farmer':
        #         return Message.objects.filter(
        #             Q(sender_farmer__user=user) | Q(recipient_farmer__user=user)
        #         ).order_by('-timestamp')
        return Message.objects.all().order_by('-timestamp')

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a specific message."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]

class ReportListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating reports."""
    queryset = Report.objects.all().order_by('-date_submitted')
    serializer_class = ReportSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter reports by the agent who submitted them (if authentication is enabled)
        # For demonstration, this returns all reports.
        # if self.request.user.is_authenticated and self.request.user.user_type == 'agent':
        #     try:
        #         agent_profile = AgentProfile.objects.get(user=self.request.user)
        #         return Report.objects.filter(agent=agent_profile).order_by('-date_submitted')
        #     except AgentProfile.DoesNotExist:
        #         return Report.objects.none()
        return Report.objects.all().order_by('-date_submitted')

    def perform_create(self, serializer):
        # Associate the report with the requesting agent (if authentication is enabled)
        # if self.request.user.is_authenticated and self.request.user.user_type == 'agent':
        #     try:
        #         agent_profile = AgentProfile.objects.get(user=self.request.user)
        #         serializer.save(agent=agent_profile)
        #     except AgentProfile.DoesNotExist:
        #         raise serializers.ValidationError("Agent profile not found for the current user.")
        # else:
        serializer.save() # For demo, save directly

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a specific report."""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    # permission_classes = [IsAuthenticated]

class GenerateReportView(APIView):
    """API endpoint to simulate report generation."""
    # permission_classes = [IsAuthenticated] # Only authenticated agents can generate reports

    def post(self, request, *args, **kwargs):
        report_type = request.data.get('report_type')
        time_period = request.data.get('time_period')

        if not report_type or not time_period:
            return Response({"message": "Report type and time period are required."}, status=status.HTTP_400_BAD_REQUEST)

        # In a real application, this would trigger a background task
        # to query the database, process data, generate a PDF/CSV, and store it.
        # For now, we just simulate the success.
        user_display = request.user.username if request.user.is_authenticated else 'Anonymous'
        print(f"Agent {user_display} requested a '{report_type}' report for '{time_period}'.")
        return Response({"message": "Report generation initiated successfully."}, status=status.HTTP_200_OK)


class AppointmentListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating appointments."""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter appointments for the logged-in agent (if authentication is enabled)
        # For demonstration, this returns all appointments.
        # if self.request.user.is_authenticated and self.request.user.user_type == 'agent':
        #     try:
        #         agent_profile = AgentProfile.objects.get(user=self.request.user)
        #         return Appointment.objects.filter(agent=agent_profile).order_by('appointment_date', 'appointment_time')
        #     except AgentProfile.DoesNotExist:
        #         return Appointment.objects.none()
        return Appointment.objects.all().order_by('appointment_date', 'appointment_time')

    def perform_create(self, serializer):
        # Associate the appointment with the requesting agent (if authentication is enabled)
        # if self.request.user.is_authenticated and self.request.user.user_type == 'agent':
        #     try:
        #         agent_profile = AgentProfile.objects.get(user=self.request.user)
        #         serializer.save(agent=agent_profile)
        #     except AgentProfile.DoesNotExist:
        #         raise serializers.ValidationError("Agent profile not found for the current user.")
        # else:
        serializer.save() # For demo, save directly

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a specific appointment."""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # permission_classes = [IsAuthenticated]
