# Generated by Django 2.2.5 on 2019-10-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanergy_leave', '0002_auto_20191002_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='Requested_Days',
            field=models.PositiveIntegerField(default=0, help_text='Total no of requested leave days'),
        ),
    ]