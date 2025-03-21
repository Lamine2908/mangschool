# Generated by Django 5.1.1 on 2025-01-03 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0025_alter_filiere_nom_alter_matiere_filiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filiere',
            name='nom',
            field=models.CharField(choices=[('Mécanique', 'Mecanique'), ('TIC', 'TIC')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='filiere',
            field=models.ForeignKey(choices=[('Mécanique', 'Mecanique'), ('TIC', 'TIC')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='auth_app.filiere'),
        ),
    ]
