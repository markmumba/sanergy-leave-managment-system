# Generated by Django 2.2.5 on 2019-10-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanergy_leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='Requested_Days',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Total no of requested leave days', null=True),
        ),
    ]
