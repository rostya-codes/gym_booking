from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('booking/', include('booking.urls')),
    path('dashboard/', include('adminpanel.urls')),
]
