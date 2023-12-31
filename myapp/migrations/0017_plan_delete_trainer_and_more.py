# Generated by Django 4.2.3 on 2023-11-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('duration', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='trainer',
        ),
        migrations.AlterField(
            model_name='addmembermodel',
            name='initialamount',
            field=models.CharField(max_length=100),
        ),
    ]
