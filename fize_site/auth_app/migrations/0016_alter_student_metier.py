# Generated by Django 5.1.4 on 2024-12-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0015_alter_enseigner_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='metier',
            field=models.CharField(blank=True, choices=[('Administration de bases de données', 'Administration de bases de données'), ('Analyse de performance digitale', 'Analyse de performance digitale'), ('Développement Front-End', 'Développement Front-End'), ('Développement Back-End', 'Développement Back-End'), ('Système, sécurité et cloud', 'Système, sécurité et cloud'), ('Réseau et Internet des objets', 'Réseau et Internet des objets')], max_length=50, null=True),
        ),
    ]
