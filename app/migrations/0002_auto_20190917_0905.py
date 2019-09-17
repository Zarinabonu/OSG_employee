# Generated by Django 2.2.5 on 2019-09-17 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='finger_print',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='scaner',
        ),
        migrations.RemoveField(
            model_name='job',
            name='employee_id',
        ),
        migrations.CreateModel(
            name='Employee_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Group')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Employee')),
            ],
        ),
    ]
