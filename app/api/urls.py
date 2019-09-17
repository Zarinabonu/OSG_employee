from django.urls import path, include

urlpatterns = [
    path('employee/', include('app.api.employee.urls')),
    path('status/', include('app.api.status.urls')),
    path('project/', include('app.api.project.urls')),

]