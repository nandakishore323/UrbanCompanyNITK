# Generated by Django 3.1.7 on 2021-10-08 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucnitk', '0002_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='CanceledTime',
        ),
        migrations.RemoveField(
            model_name='order',
            name='OrderFinishedTime',
        ),
    ]
