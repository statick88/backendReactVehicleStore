# Generated by Django 4.2.2 on 2024-03-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(upload_to='vehicle_images/'),
        ),
    ]
