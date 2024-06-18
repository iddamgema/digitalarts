# Generated by Django 4.2.7 on 2024-06-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_order_pickup_point_trackingorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('paypal', 'Paypal'), ('mpesa', 'Mpesa')], default='mpesa', max_length=100),
        ),
        migrations.AlterField(
            model_name='trackingorders',
            name='status',
            field=models.CharField(choices=[('arrived', 'arrived'), ('ontransit', 'On Transit'), ('packaging', 'Packaging')], default='packaging', max_length=100),
        ),
    ]
