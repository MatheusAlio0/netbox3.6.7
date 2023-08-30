# Generated by Django 4.1.10 on 2023-08-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0181_rename_device_role_device_role'),
        ('ipam', '0067_ipaddress_index_host'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='l2vpntermination',
            name='ipam_l2vpntermination_assigned_object',
        ),
        migrations.AddField(
            model_name='l2vpntermination',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l2vpns', to='dcim.device'),
        ),
        migrations.AddConstraint(
            model_name='l2vpntermination',
            constraint=models.UniqueConstraint(fields=('device', 'assigned_object_type', 'assigned_object_id'), name='ipam_l2vpntermination_device_assigned_object'),
        ),
        migrations.AddConstraint(
            model_name='l2vpntermination',
            constraint=models.UniqueConstraint(condition=models.Q(('device__isnull', True)), fields=('assigned_object_type', 'assigned_object_id'), name='ipam_l2vpntermination_assigned_object', violation_error_message='This object is already assigned to this l2vpn without a device specified'),
        ),
    ]
