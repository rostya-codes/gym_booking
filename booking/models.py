from django.conf import settings
from django.db import models
from django.db.models import ForeignKey

User = settings.AUTH_USER_MODEL


class Slot(models.Model):
    date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Date of Slot"
    )

    start_time = models.TimeField(
        verbose_name="Start Time",
        help_text="Time when the slot starts (hh:mm)"
    )

    end_time = models.TimeField(
        verbose_name="End Time",
        help_text="Time when the slot ends (hh:mm)"
    )

    room = models.CharField(max_length=50)

    is_available = models.BooleanField(
        default=True,
        verbose_name='Is available'
    )

    created_by = models.ForeignKey(
        User,  # або 'auth.User' якщо не кастомна модель
        on_delete=models.SET_NULL,  # або models.CASCADE, якщо хочеш видаляти разом з юзером
        null=True,  # щоб дозволити порожнє значення (наприклад, при автостворенні)
        blank=True,  # дозволяє залишити поле пустим у формах
        verbose_name="Created by",  # назва у панелі адміністратора
        related_name="created_slots"  # дозволяє отримати всі слоти, створені цим юзером
    )

    notes = models.TextField()

    def __str__(self):
        return f'{self.room}: {self.date}, created by {self.created_by}'


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="bookings"
    )
    slot = models.ForeignKey(
        'Slot',
        on_delete=models.CASCADE,
        verbose_name="Slot",
        related_name="slot_bookings"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"Booking by {self.user.username} for {self.slot}"
