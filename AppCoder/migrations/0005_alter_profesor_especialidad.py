# Generated by Django 5.0.3 on 2024-04-14 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alumno_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='especialidad',
            field=models.CharField(max_length=100),
        ),
    ]