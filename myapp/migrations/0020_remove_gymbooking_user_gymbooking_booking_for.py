# Generated by Django 4.2.3 on 2023-11-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_gymbooking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymbooking',
            name='user',
        ),
        migrations.AddField(
            model_name='gymbooking',
            name='booking_for',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
