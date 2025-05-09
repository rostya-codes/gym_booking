from django.urls import path

from . import views

urlpatterns = [
    path('schedule/', views.schedule_view, name='schedule'),
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),
    path('book/<int:slot_id>/', views.book_slot_view, name='book_slot'),
    path('cancel/<int:booking_id>/', views.cancel_booking_view, name='cancel_booking'),
]
