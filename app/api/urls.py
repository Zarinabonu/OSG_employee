from django.urls import path, include

urlpatterns = [
    path('employee/', include('app.api.employee.urls')),
    # path('project/', include('app.api.project.urls')),

]