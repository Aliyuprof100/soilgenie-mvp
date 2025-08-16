# users/urls.py
from django.urls import path
from .views import FarmerRegisterView, AgentRegisterView, LoginView, LogoutView, UserProfileView

urlpatterns = [
    path('register/farmer/', FarmerRegisterView.as_view(), name='farmer_register'),
    path('register/agent/', AgentRegisterView.as_view(), name='agent_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
