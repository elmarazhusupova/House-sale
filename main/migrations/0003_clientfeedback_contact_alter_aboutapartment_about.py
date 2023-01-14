# Generated by Django 4.1.5 on 2023-01-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aboutapartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('feedback', models.TextField(verbose_name='Отзыв')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='aboutapartment',
            name='about',
            field=models.TextField(verbose_name='О нашей квартире'),
        ),
    ]