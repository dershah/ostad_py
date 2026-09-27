from django.urls import path
from . import views

urlpatterns = [
    path('request/<int:property_id>/', views.create_rental_request, name='create_rental_request'),
    path('request/<int:pk>/cancel/', views.cancel_rental_request, name='cancel_rental_request'),
    path('request/<int:pk>/<str:action>/', views.update_request_status, name='update_request_status'),
    path('dashboard/owner/', views.owner_dashboard, name='owner_dashboard'),
    path('dashboard/tenant/', views.tenant_dashboard, name='tenant_dashboard'),
    path('review/<int:property_id>/', views.create_review, name='create_review'),
]
