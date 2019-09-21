from django.urls import path, include

# from app.api.employee import views
from app.api.employee import views

urlpatterns = [
    path('create/', views.Employee_createAPIView.as_view(), name='api-employee-create'),
    path('update/<int:id>', views.Employee_updateAPIView.as_view(), name='api-employee-update'),
    path('delete/<int:id>', views.Employee_deleteAPIView.as_view(), name='api-employee-delete'),
    path('list/', views.Employee_listAPIView.as_view(), name='api-employee-list'),
    path('group/create', views.Employee_groupCreateapiView.as_view(), name='api-project-group-create'),
    # path('group/update/<int:id>', views.Group_updateAPIView.as_view(), name='api-project-group-update'),
    # path('group/delete/<int:id>', views.Group_deleteAPIView.as_view(), name='api-project-group-delete'),
    # path('group/list', views.Group_listAPIView.as_view(), name='api-project-group-list'),

]