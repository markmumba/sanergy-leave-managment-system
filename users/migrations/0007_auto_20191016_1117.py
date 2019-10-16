# Generated by Django 2.2.5 on 2019-10-16 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191015_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('user_id',)},
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sanergy_leave.Department'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
