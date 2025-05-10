from django import forms

from booking.models import Slot


class CreateSlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ('date', 'start_time', 'end_time', 'room', 'is_available')
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'start_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
        }
