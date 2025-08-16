from django.shortcuts import render

# Create your views here.
# recommendations/views.py
from rest_framework import generics
from .models import Recommendation
from .serializers import RecommendationSerializer
# from rest_framework.permissions import IsAuthenticated # Uncomment when auth is ready

class RecommendationListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating recommendations."""
    queryset = Recommendation.objects.all().order_by('-date_issued') # Order by latest
    serializer_class = RecommendationSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter recommendations by agent's assigned farmers
        # For demo, returning all
        # if self.request.user.user_type == 'agent':
        #     # This logic needs to be refined based on how agents are assigned to farmers
        #     return Recommendation.objects.filter(farmland__farmer__agent_profile__user=self.request.user).order_by('-date_issued')
        return Recommendation.objects.all().order_by('-date_issued')

class RecommendationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a specific recommendation."""
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    # permission_classes = [IsAuthenticated]
