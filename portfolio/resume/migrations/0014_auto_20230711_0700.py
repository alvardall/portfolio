# Generated by Django 2.2.12 on 2023-07-11 07:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_fact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
    ]
