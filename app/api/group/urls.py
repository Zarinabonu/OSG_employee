from django.urls import path

from app.api.group import views

urlpatterns = [
    # path('create', views.Position_createAPIView.as_view(), name='api-status-create'),
    path('list', views.Egroup_listAPIView.as_view(), name='api-group-list')

]