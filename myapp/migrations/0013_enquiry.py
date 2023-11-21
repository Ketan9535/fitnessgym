# Generated by Django 4.2.3 on 2023-10-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_faq_delete_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
