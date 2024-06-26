from django.urls import path
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, register, car_list_json

urlpatterns = [
    path('register/', register, name='register'),
    path('cars/', CarListView.as_view(), name='car-list'),
    path('api/cars/', car_list_json, name='car-list-json'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    
]
