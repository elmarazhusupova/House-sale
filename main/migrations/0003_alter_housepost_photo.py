# Generated by Django 4.1.5 on 2023-02-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_housepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housepost',
            name='photo',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
