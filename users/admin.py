# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, FarmerProfile, AgentProfile
# from farms.models import Farmland # REMOVED: No longer needed here as FarmlandAdmin is moved

# Register your custom User model
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    # Add 'user_type', 'phone_number', 'location' to the list display in admin
    list_display = BaseUserAdmin.list_display + ('user_type', 'phone_number', 'location')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type', 'phone_number', 'location')}),
    )

# Register FarmerProfile
@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'farm_location_detail', 'farm_size_hectares')
    search_fields = ('user__username', 'farm_location_detail')

# Register AgentProfile
@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_area', 'qualification')
    search_fields = ('user__username', 'service_area')

# REMOVED: FarmlandAdmin registration moved to farms/admin.py to avoid AlreadyRegistered error
# @admin.register(Farmland)
# class FarmlandAdmin(admin.ModelAdmin):
#     list_display = ('farmer', 'farm_name', 'location_detail', 'area_hectares', 'intended_crop_type', 'date_added')
#     list_filter = ('intended_crop_type',)
#     search_fields = ('farmer__user__username', 'farm_name', 'location_detail')
#     # You can add more features like:
#     # list_editable = ('area_hectares', 'intended_crop_type') # Allows editing directly from list view
#     # raw_id_fields = ('farmer',) # For large number of farmers, use ID input


# --- Important: Also register other models from other apps if you want to see them ---
# Example for other apps (uncomment and move to respective admin.py files as needed):
# from recommendations.models import Recommendation
# @admin.register(Recommendation)
# class RecommendationAdmin(admin.ModelAdmin):
#     list_display = ('farmland', 'recommendation_type', 'status', 'date_issued')
#     list_filter = ('recommendation_type', 'status')
#     search_fields = ('farmland__farmer__user__username', 'recommendation_text')

# from agents.models import Task, Message, Report, Appointment
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'agent', 'farmer', 'due_date', 'status')
#     list_filter = ('status', 'agent')
#     search_fields = ('title', 'agent__user__username', 'farmer__user__username')

# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'sender_agent', 'sender_farmer', 'recipient_agent', 'recipient_farmer', 'timestamp', 'is_read')
#     list_filter = ('is_read',)
#     search_fields = ('message_content',)

# @admin.register(Report)
# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('report_type', 'agent', 'farmer', 'date_submitted')
#     list_filter = ('report_type', 'agent')
#     search_fields = ('report_summary',)

# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('farmer', 'agent', 'appointment_date', 'appointment_time', 'is_completed')
#     list_filter = ('is_completed', 'appointment_date')
#     search_fields = ('farmer__user__username', 'agent__user__username', 'purpose')
