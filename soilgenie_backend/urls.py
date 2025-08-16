# soilgenie_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # Import TemplateView
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # API endpoints for your apps
    path('api/users/', include('users.urls')),
    path('api/farmlands/', include('farms.urls')),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/agents/', include('agents.urls')),

    # Serve your frontend HTML pages directly
    # IMPORTANT: Ensure these HTML files exist directly in your 'frontend' folder
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login_selection.html', TemplateView.as_view(template_name='login_selection.html'), name='login_selection'),
    path('signup_selection.html', TemplateView.as_view(template_name='signup_selection.html'), name='signup_selection'),
    path('farmer_signup.html', TemplateView.as_view(template_name='farmer_signup.html'), name='farmer_signup'),
    path('agent_signup.html', TemplateView.as_view(template_name='agent_signup.html'), name='agent_signup'),
    path('farmer_dashboard.html', TemplateView.as_view(template_name='farmer_dashboard.html'), name='farmer_dashboard'),
    path('agent_dashboard.html', TemplateView.as_view(template_name='agent_dashboard.html'), name='agent_dashboard'),
    path('farmer_login.html', TemplateView.as_view(template_name='farmer_login.html'), name='farmer_login'),
    path('agent_login.html', TemplateView.as_view(template_name='agent_login.html'), name='agent_login'),
]

# Only serve static files this way in development. In production, use a proper web server.
if settings.DEBUG:
    # This line tells Django's development server to serve static files from STATICFILES_DIRS
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

