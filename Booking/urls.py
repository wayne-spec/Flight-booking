from django.urls import path
from .views import (FlightListCreateView,FlightRetrieveUpdateDeleteView,PassengerListCreateView, PassengerRetrieveUpdateDeleteView)

urlpatterns = [
    # Flight URLs
    path('flights/', FlightListCreateView.as_view(), name='flight-list-create'),
    path('flights/<int:pk>/', FlightRetrieveUpdateDeleteView.as_view(), name='flight-detail'),

    # Passenger URLs
    path('passengers/', PassengerListCreateView.as_view(), name='passenger-list-create'),
    path('passengers/<int:pk>/', PassengerRetrieveUpdateDeleteView.as_view(), name='passenger-detail'),
]
