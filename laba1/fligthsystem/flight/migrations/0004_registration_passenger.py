# Generated by Django 5.1.4 on 2025-03-17 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='passenger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flight.passenger'),
        ),
    ]
