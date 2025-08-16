# farms/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Farmland
from .serializers import FarmlandSerializer
# from rest_framework.permissions import IsAuthenticated # Uncomment when authentication is set up

class FarmlandListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing all farmlands or creating a new farmland.
    """
    queryset = Farmland.objects.all().order_by('-date_added') # Order by latest added first
    serializer_class = FarmlandSerializer
    # permission_classes = [IsAuthenticated] # Uncomment this when users are authenticated

    def get_queryset(self):
        """
        Optionally filters farmlands by the logged-in user if they are a farmer.
        For demonstration, currently returns all farmlands.
        """
        # If you want to filter by the logged-in farmer, uncomment the following:
        # user = self.request.user
        # if user.is_authenticated and hasattr(user, 'farmer_profile'):
        #     return Farmland.objects.filter(farmer=user.farmer_profile).order_by('-date_added')
        return Farmland.objects.all().order_by('-date_added')

    def perform_create(self, serializer):
        """
        Saves the new farmland. The 'farmer' field is now handled directly by the serializer,
        expecting a valid FarmerProfile ID in the request data.
        Any validation errors (e.g., invalid farmer_id) will be caught by serializer.is_valid().
        """
        print(f"--- perform_create called: Attempting to save farmland ---")
        try:
            # The serializer's `farmer` field handles finding the FarmerProfile object
            # based on the `farmer_id` sent in the request data.
            serializer.save()
            print(f"--- Farmland saved successfully by serializer.save()! ---")
        except Exception as e:
            print(f"--- ERROR during serializer.save() in perform_create: {e} ---")
            # Re-raise the exception to trigger an appropriate HTTP 500 response if needed
            raise


    def create(self, request, *args, **kwargs):
        print(f"--- Received POST request for Farmland creation ---")
        print(f"Request data: {request.data}") # Log incoming request data
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            print(f"--- Serializer is VALID. Data: {serializer.validated_data} ---")
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print(f"--- Farmland creation successful. Returning 201 response. ---")
            return Response(
                {"message": "Farm mapped successfully! Data saved.", "data": serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except Exception as e:
            print(f"--- ERROR in create method: {e} ---")
            print(f"Serializer errors: {serializer.errors}") # Log detailed serializer errors
            return Response(
                {"message": "Error mapping farm. Please check your input.", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST # Or 500 depending on error type
            )

class FarmlandDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific farmland.
    """
    queryset = Farmland.objects.all()
    serializer_class = FarmlandSerializer
    # permission_classes = [IsAuthenticated] # Restrict access to authenticated users
    # lookup_field = 'pk' # Default, but good to be explicit
