# farms/serializers.py
from rest_framework import serializers
from .models import Farmland
from users.models import FarmerProfile # Ensure FarmerProfile is imported

class FarmlandSerializer(serializers.ModelSerializer):
    # This field accepts the farmer's profile ID (PK) for creation/update.
    # DRF will automatically look up the FarmerProfile instance based on this ID.
    farmer = serializers.PrimaryKeyRelatedField(queryset=FarmerProfile.objects.all())

    class Meta:
        model = Farmland
        fields = (
            'id', 'farmer', 'farm_name', 'location_detail', 'area_hectares',
            'intended_crop_type', 'notes', 'geojson_data', 'date_added', 'last_updated'
        )
        read_only_fields = ('id', 'date_added', 'last_updated') # 'id' is also read-only