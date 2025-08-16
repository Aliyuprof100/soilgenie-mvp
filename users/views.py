# users/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

# Corrected imports for serializers
from .serializers import (
    UserProfileSerializer,        # Used for profile view
    FarmerRegisterSerializer,     # Used for farmer registration
    AgentRegisterSerializer,      # Used for agent registration
    LoginSerializer               # Used for login
)
from users.models import User, FarmerProfile, AgentProfile # Import models

# Authentication specific imports
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token

class FarmerRegisterView(generics.CreateAPIView):
    """API endpoint for farmer registration."""
    queryset = User.objects.all()
    serializer_class = FarmerRegisterSerializer
    permission_classes = [AllowAny] # Allow anyone to register

class AgentRegisterView(generics.CreateAPIView):
    """API endpoint for agent registration."""
    queryset = User.objects.all()
    serializer_class = AgentRegisterSerializer
    permission_classes = [AllowAny] # Allow anyone to register

class LoginView(APIView):
    """API endpoint for user login."""
    permission_classes = [AllowAny] # Allow anyone to attempt login

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
                # --- CRITICAL FIX START ---
                # Use UserProfileSerializer to get consistent user data,
                # which correctly includes farmer_profile_id/agent_profile_id via SerializerMethodField.
                user_data_serializer = UserProfileSerializer(user)
                response_data = {
                    'message': 'Login successful',
                    'user': user_data_serializer.data, # This now contains id, username, user_type, farmer_profile_id etc.
                    'csrf_token': get_token(request) # Include CSRF token in login response
                }
                # --- CRITICAL FIX END ---

                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    """API endpoint for user logout."""
    permission_classes = [IsAuthenticated] # Only logged-in users can logout

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveAPIView):
    """API endpoint for retrieving current user's profile."""
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access their profile

    def get_object(self):
        # The request.user is automatically set by Django's authentication middleware
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        response_data = serializer.data
        # Ensure farmer_profile_id and agent_profile_id are always present, even if None
        response_data['farmer_profile_id'] = response_data.get('farmer_profile_id')
        response_data['agent_profile_id'] = response_data.get('agent_profile_id')
        
        return Response(response_data)
