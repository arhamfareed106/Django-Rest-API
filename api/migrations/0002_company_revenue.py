# Generated by Django 5.1.3 on 2024-11-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='revenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
