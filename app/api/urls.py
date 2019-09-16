from django.urls import path, include

urlpatterns = [
    path('employees/', include('app.api.employee.urls')),
]