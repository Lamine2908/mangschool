# Generated by Django 5.1.3 on 2024-11-17 04:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_responsablemetier_administrateur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planning',
            name='activite1',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='activite2',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='activite3',
        ),
        migrations.AddField(
            model_name='planning',
            name='matiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.matiere'),
        ),
    ]
