# Generated by Django 3.1.7 on 2021-10-17 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('I_Status', models.CharField(choices=[('Resolved', 'Resolved'), ('Pending', 'Pending')], default='Pending', max_length=15)),
                ('I_type', models.CharField(choices=[('Order Not being Accepted/Delivered', 'Order Not being Accepted/Delivered'), ('Issue With Service Provider', 'Issue With Service Provider'), ('Order Says Delivered but have not recieved anything', 'Order Says Delivered but have not recieved anything'), ('Other', 'Other')], default='Other', max_length=100)),
                ('I_details', models.CharField(default='Nothing', max_length=100)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Help_Customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('ServiceName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MinPrice', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField(default=100)),
                ('FromLocation', models.TextField()),
                ('Description', models.TextField()),
                ('QueuedTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('AcceptedTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('CompletedTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('ServiceType', models.CharField(choices=[('Electrician', 'Electrician'), ('Cleaner', 'Cleaner'), ('Salon', 'Salon'), ('Laundry', 'Laundry'), ('Delivery', 'Delivery'), ('Plumber', 'Plumber')], default='Laundry', max_length=15)),
                ('PreferredTime', models.CharField(choices=[('Anytime', 'Anytime'), ('10AM-12PM', '10AM-12PM'), ('2PM-5PM', '2PM-5PM'), ('5PM-8PM', '5PM-8PM')], default='Anytime', max_length=15)),
                ('Status', models.CharField(choices=[('Not Accepted', 'Not Accepted'), ('Accepted', 'Accepted'), ('Pending Payment', 'Pending Payment'), ('Completed', 'Completed')], default='Not Accepted', max_length=15)),
                ('payment_status', models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING')], default=3)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.IntegerField(default=1)),
                ('review', models.CharField(blank=True, max_length=250, null=True)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL)),
                ('ServiceProvider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ServiceProvider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='help/')),
                ('help', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucnitk.help')),
            ],
        ),
        migrations.AddField(
            model_name='help',
            name='OrderWh',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Order_Wh', to='ucnitk.order'),
        ),
    ]
