from django.urls import path

from app.api.project import views

urlpatterns = [
    path('create', views.Project_createAPIView.as_view(), name='api-project-create'),
    path('update/<int:id>', views.Project_updateAPIView.as_view(), name='api-status-update')

]