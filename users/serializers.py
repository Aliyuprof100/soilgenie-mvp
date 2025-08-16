# users/serializers.py
from rest_framework import serializers
from .models import User, FarmerProfile, AgentProfile # Ensure AgentProfile is also imported

class UserProfileSerializer(serializers.ModelSerializer):
    # This field will be dynamically set based on user_type
    farmer_profile_id = serializers.SerializerMethodField()
    agent_profile_id = serializers.SerializerMethodField() # Also include for agents if needed

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'location', 'user_type', 'farmer_profile_id', 'agent_profile_id')
        read_only_fields = ('id', 'username', 'email', 'user_type')

    def get_farmer_profile_id(self, obj):
        # Return the primary key of the FarmerProfile if the user is a farmer
        if obj.user_type == 'farmer' and hasattr(obj, 'farmer_profile'):
            return obj.farmer_profile.pk
        return None

    def get_agent_profile_id(self, obj):
        # Return the primary key of the AgentProfile if the user is an agent
        if obj.user_type == 'agent' and hasattr(obj, 'agent_profile'):
            return obj.agent_profile.pk
        return None

class FarmerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    farm_location_detail = serializers.CharField(write_only=True, required=False, allow_blank=True)
    farm_size_hectares = serializers.FloatField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'location', 'password', 'confirm_password', 'farm_location_detail', 'farm_size_hectares')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Extract farmer profile specific data
        farm_location_detail = validated_data.pop('farm_location_detail', None)
        farm_size_hectares = validated_data.pop('farm_size_hectares', None)
        validated_data.pop('confirm_password') # Remove confirm_password as it's not part of User model

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            location=validated_data.get('location'),
            user_type='farmer'
        )
        FarmerProfile.objects.create(
            user=user,
            farm_location_detail=farm_location_detail,
            farm_size_hectares=farm_size_hectares
        )
        return user

class AgentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    service_area = serializers.CharField(write_only=True, required=False, allow_blank=True)
    qualification = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'location', 'password', 'confirm_password', 'service_area', 'qualification')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Extract agent profile specific data
        service_area = validated_data.pop('service_area', None)
        qualification = validated_data.pop('qualification', None)
        validated_data.pop('confirm_password') # Remove confirm_password

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            location=validated_data.get('location'),
            user_type='agent'
        )
        AgentProfile.objects.create(
            user=user,
            service_area=service_area,
            qualification=qualification
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
