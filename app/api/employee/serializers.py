# Employee va EmployeeGroup serializerlarini shu yerga yozing



# from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
# from django.contrib.auth.models import User
#
# from rest_framework import serializers
#
#
#
# class EmployeeSerializer(ModelSerializer):
#     status = StatusSerialzer(read_only=True)
#     username = serializers.CharField(write_only=True)
#     first_name = serializers.CharField(write_only=True)
#     last_name = serializers.CharField(write_only=True)
#     email = serializers.EmailField(write_only=True)
#     is_active = serializers.BooleanField(write_only=True)
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ('image',
#                   'phone',
#                   'address',
#                   'status',
#                   'username',
#                   'first_name',
#                   'last_name',
#                   'email',
#                   'is_active',
#                   'password',
#                   )
#
#     def create(self, validated_data):
#         username = validated_data.pop('username')
#     #     _id = serializers.IntegerField(write_only=True)
#         firstname = validated_data.pop('first_name')
#         lastname = validated_data.pop('last_name')
#         email = validated_data.pop('email')
#         is_active = validated_data.pop('is_active')
#         password = validated_data('password')
#     #
#         employee = Employee(**validated_data)
#         u = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email, is_active=is_active)
#         u.set_password(password)
#         u.save()
#         employee.user = u
#         employee.save()
#         return employee
#
#     def update(self, instance, validated_data):
#         raise_errors_on_nested_writes('update', self, validated_data)
#
#         if validated_data.get('password'):
#             p = validated_data.pop('password')
#             instance.user.set_password(p)
#         for attr, value in validated_data.items():
#             setattr(instance.user, attr, value)
#         instance.user.save()
#         instance.save()
#
#         return instance
#
#
# class Employee_userlistSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username',
#                   'first_name',
#                   'last_name',
#                   'email')
#
#
# class Employee_salarylistSerializer(ModelSerializer):
#     class Meta:
#         model = Employee_salary
#         fields = ('salary',)
#
#
# class Group_Serialzier(ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('group_name',)
#
#
# class Employee_groupSerialzier(ModelSerializer):
#     employee_group = Group_Serialzier()
#
#     class Meta:
#         model = Employee_group
#         fields = ('employee_group',)
#
#
# class Employee_listSerializer(ModelSerializer):
#     employee_salary = Employee_salarylistSerializer(read_only=True)
#     user = Employee_userlistSerializer()
#     employee_group_set = Employee_groupSerialzier(many=True, read_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ('image',
#                   'phone',
#                   'address',
#                   'status',
#                   'user',
#                   'employee_salary',
#                   'employee_group_set')
#
#     def to_representation(self, instance):
#         print(instance.employee_salary.id)
#         employee_status = super(Employee_listSerializer, self).to_representation(instance)
#         print('111', employee_status)
#         if instance.status.degree == 9:
#             employee_status.pop('employee_salary')
#         elif instance.status.degree == 8:
#             employee_status.pop('employee_salary')
#             employee_status.pop('employee_group_set')
#
#         elif instance.status.degree == 7:
#             employee_status.pop('employee_group_set')
#         elif instance.status.degree == 6:
#             employee_status.pop('image',
#                                 'phone',
#                                 'address',
#                                 'status',
#                                 'user',
#                                 'employee_salary',
#                                 'employee_group_set')
#
#         return employee_status
#
#
# class Employee_salarySerialzer(ModelSerializer):
#     class Meta:
#         model = Employee_salary
#         fields = ('employee_id',
#                   'salary')
#
#     def update(self, instance, validated_data):
#         instance.employee_id = self.context['request'].data.get('employee_id')
#         instance.salary = self.context['request'].data.get('salary')
#
#         instance.save()
#         return instance
#
#
#
#
#
