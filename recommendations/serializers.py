# recommendations/serializers.py
from rest_framework import serializers
from .models import Recommendation
from farms.models import Farmland # Import Farmland from the farms app
from users.models import FarmerProfile # Import FarmerProfile from the users app

class RecommendationSerializer(serializers.ModelSerializer):
    # farmland_details = FarmlandSerializer(source='farmland', read_only=True) # For nested display
    farmland_id = serializers.PrimaryKeyRelatedField(
        queryset=Farmland.objects.all(), source='farmland', write_only=True
    )
    farmer_username = serializers.CharField(source='farmland.farmer.user.username', read_only=True)
    crop_type = serializers.CharField(source='farmland.intended_crop_type', read_only=True)

    class Meta:
        model = Recommendation
        fields = (
            'id', 'farmland_id', 'farmer_username', 'crop_type', 'recommendation_type',
            'recommendation_text', 'date_issued', 'status', 'agent_notes'
        )
        read_only_fields = ('date_issued',)
