from django.urls import path

from app.api.project import views

urlpatterns = [
    path('create', views.Project_createAPIView.as_view(), name='api-project-create'),
    path('update/<int:id>', views.Project_updateAPIView.as_view(), name='api-project-update'),
    path('delete/<int:id>', views.Project_deleteAPIView.as_view(), name='api-project-delete'),
    path('list', views.Project_listAPIView.as_view(), name='api-project-list'),
    path('group/create', views.Group_createAPIView.as_view(), name='api-project-group-create'),
    path('group/update/<int:id>', views.Group_updateAPIView.as_view(), name='api-project-group-update'),
    path('group/delete/<int:id>', views.Group_deleteAPIView.as_view(), name='api-project-group-delete'),
    path('group/list', views.Group_listAPIView.as_view(), name='api-project-group-list'),

]