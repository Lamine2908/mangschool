# Generated by Django 5.0.7 on 2024-10-03 07:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0090_alter_planning_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
