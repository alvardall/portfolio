# Generated by Django 4.2.4 on 2023-08-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_portfolioproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='icon_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
