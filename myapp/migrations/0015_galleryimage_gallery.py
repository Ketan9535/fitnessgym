# Generated by Django 4.2.3 on 2023-10-31 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_gallery_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='gallery',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.gallery'),
            preserve_default=False,
        ),
    ]
