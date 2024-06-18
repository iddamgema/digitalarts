# Generated by Django 4.2.7 on 2024-06-10 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0021_shipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='created_at',
            new_name='shipped_at',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='shipped',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='order',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shipment',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
