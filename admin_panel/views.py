from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from admin_panel.forms import CreateSlotForm

User = get_user_model()


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff, login_url='index')
def admin_dashboard_view(request):
    return render(request, 'admin_panel/dashboard.html')


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff, login_url='index')
def add_slot_view(request):
    if request.method == 'POST':
        form = CreateSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slot successfully created.', extra_tags='success')
            return redirect('dashboard')
    else:
        form = CreateSlotForm()

    return render(request, 'admin_panel/slot_add.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff, login_url='index')
def users_list_view(request):
    users = User.objects.all()
    return render(request, 'admin_panel/users_list.html', {'users': users})
