# farms/urls.py
from django.urls import path
from .views import FarmlandListCreateView, FarmlandDetailView

urlpatterns = [
    path('', FarmlandListCreateView.as_view(), name='farmland-list-create'),
    path('<int:pk>/', FarmlandDetailView.as_view(), name='farmland-detail'),
]