# agents/urls.py
from django.urls import path
from .views import (
    TaskListCreateView, TaskDetailView,
    MessageListCreateView, MessageDetailView,
    ReportListCreateView, ReportDetailView,
    GenerateReportView,
    AppointmentListCreateView, AppointmentDetailView
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('reports/', ReportListCreateView.as_view(), name='report-list-create'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('reports/generate/', GenerateReportView.as_view(), name='generate-report'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]
