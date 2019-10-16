# Generated by Django 2.2.5 on 2019-10-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanergy_leave', '0002_auto_20191015_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='leave',
            name='leave_balance',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='Leave_Types',
            field=models.CharField(choices=[('MATERNITY_LEAVE', 'MATERNITY_LEAVE'), ('PATERNITY_LEAVE', 'PATERNITY_LEAVE'), ('ANNUAL_LEAVE', 'ANNUAL_LEAVE'), ('COMPASSIONATE_LEAVE', 'COMPASSIONATE_LEAVE'), ('SICK_LEAVE', 'SICK_LEAVE'), ('STUDY_LEAVE', 'STUDY_LEAVE')], default='ANNUAL_LEAVE', max_length=20),
        ),
    ]
