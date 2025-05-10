from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from booking.models import Slot, Booking


def schedule_view(request):
    slots = Slot.objects.filter(date__gte=timezone.now().date()).order_by('date', 'start_time')
    return render(request, 'booking/schedule.html', {'slots': slots})


@login_required(login_url='login')
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})


@login_required(login_url='login')
def book_slot_view(request, slot_id):
    slot = get_object_or_404(Slot, pk=slot_id)

    if not slot.is_available:
        messages.error(request, 'This slot has already been booked.', extra_tags='danger')
        return redirect('schedule')

    Booking.objects.create(user=request.user, slot=slot)
    slot.is_available = False
    slot.save()

    return render(request, 'booking/booking_success.html')


@login_required(login_url='login')
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if booking.user != request.user:
        messages.error(request, "You do not have permission to cancel this booking.")
        return redirect('my_bookings')

    booking.slot.is_available = True
    booking.slot.save()
    booking.delete()
    messages.success(request, 'Your booking has been canceled.', extra_tags='success')
    return redirect('my_bookings')
