# Generated by Django 4.2.3 on 2023-10-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField()),
                ('ans', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
    ]
