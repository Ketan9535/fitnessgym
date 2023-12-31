# Generated by Django 4.2.3 on 2023-10-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_banners'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='cat_imgs/')),
            ],
            options={
                'verbose_name_plural': '2.Catogories',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='services/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name_plural': '1.Banners'},
        ),
        migrations.AlterField(
            model_name='banners',
            name='alt_text',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='banners',
            name='img',
            field=models.ImageField(upload_to='banners_imgs/'),
        ),
    ]
