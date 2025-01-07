from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('event_management_system_app.urls')),  # Include your app's URLs
]
