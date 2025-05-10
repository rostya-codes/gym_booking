from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard_view, name='dashboard'),
    path('add-slot/', views.add_slot_view, name='add_slot'),
    path('users/', views.users_list_view, name='users_list'),
]
