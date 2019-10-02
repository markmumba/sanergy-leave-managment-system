# Generated by Django 2.2.5 on 2019-10-01 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(default='Service', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employment_Terms', models.CharField(choices=[('PERMANENT', 'PERMANENT'), ('PARTTIME', 'PARTTIME'), ('PROBATIONARY', 'PROBATIONARY')], default='probationary', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_Types', models.CharField(choices=[('EXPECTANCY', 'EXPECTANCY'), ('ANNUAL_LEAVE', 'ANNUAL_LEAVE'), ('MILITARY_LEAVE', 'MILITARY_LEAVE'), ('EDUCATION_LEAVE', 'EDUCATION_LEAVE')], default='annual', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='Emergency Notice', max_length=100)),
                ('message', models.TextField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('Begin_Date', models.DateField(help_text='Leave begin date')),
                ('End_Date', models.DateField(help_text='Leave end date')),
                ('Requested_Days', models.PositiveIntegerField(default=5, help_text='Total no of requested leave days')),
                ('leave_status', models.IntegerField(choices=[(0, 'Approved'), (1, 'Pending'), (2, 'Declined')], default=1)),
                ('Comments', models.CharField(max_length=500, null=True)),
                ('Leave_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanergy_leave.LeaveType')),
                ('leave_issuer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leave_issuer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-leave_id',),
            },
        ),
    ]
