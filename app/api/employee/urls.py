from django.urls import path, include

from app.api.employee import views

urlpatterns = [
    path('create/', views.Employee_createAPIView.as_view(), name='api-employee-create'),
    path('update/<int:id>', views.Employee_updateAPIView.as_view(), name='api-employee-update'),
    path('delete/<int:id>', views.Employee_deleteAPIView.as_view(), name='api-employee-delete'),
    path('list/', views.Employee_listAPIView.as_view(), name='api-employee-list'),
    path('salary/create/', views.Employee_salaryAPIView.as_view(), name='api-employee-salary-create'),
    path('salary/update/<int:id>', views.Employee_salaryAPIView.as_view(), name='api-employee-salary-update'),

]