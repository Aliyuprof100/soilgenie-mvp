# farms/admin.py
from django.contrib import admin
from .models import Farmland

# Register Farmland in its own app's admin.py
@admin.register(Farmland)
class FarmlandAdmin(admin.ModelAdmin):
    # Corrected list_display to use 'date_added'
    list_display = ('farmer', 'farm_name', 'location_detail', 'area_hectares', 'intended_crop_type', 'date_added')
    # Corrected list_filter to use 'date_added'
    list_filter = ('intended_crop_type', 'date_added') 
    search_fields = ('farmer__user__username', 'farm_name', 'location_detail')
    # Corrected readonly_fields to use 'date_added'
    readonly_fields = ('date_added', 'last_updated') 

    # You can add more features like:
    # list_editable = ('area_hectares', 'intended_crop_type') # Allows editing directly from list view
    # raw_id_fields = ('farmer',) # For large number of farmers, use ID input
