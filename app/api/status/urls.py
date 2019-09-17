from django.urls import path

from app.api.status import views

urlpatterns = [
    path('create', views.Status_createAPIView.as_view(), name='api-status-create'),
    path('list', views.Status_listAPIView.as_view(), name='api-status-list')

]