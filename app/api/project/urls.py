from django.urls import path

from app.api.project import views

urlpatterns = [

    path('group/create', views.Group_createAPIView.as_view(), name='api-project-group-create'),
    path('group/update/<int:id>', views.Group_updateAPIView.as_view(), name='api-project-group-update'),
    path('group/delete/<int:id>', views.Group_deleteAPIView.as_view(), name='api-project-group-delete'),
    path('group/list', views.Group_listAPIView.as_view(), name='api-project-group-list'),
    path('task/create', views.Task_createAPIView.as_view(), name='api-project-task-create'),
    path('task/update/<int:id>', views.Task_updateAPIView.as_view(), name='api-project-task-update'),
    path('task/delete/<int:id>', views.Task_deleteAPIView.as_view(), name='api-project-task-delete'),
    path('list', views.Project_listAPIView.as_view(), name='api-project-list')
    # path('group/list', views.Group_listAPIView.as_view(), name='api-project-group-list'),
]