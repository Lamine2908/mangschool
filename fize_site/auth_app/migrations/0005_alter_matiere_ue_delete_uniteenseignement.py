# Generated by Django 5.1.3 on 2024-11-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_student_metier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='ue',
            field=models.CharField(choices=[('Informatique', 'Appliquer les bases en informatique'), ('Génie Logiciel', 'Initialisation au Génie Logiciel'), ('Communication', 'Découvrir le milieu professionnel'), ('Mathématiques', 'bases en mathématiques'), ('Projet', 'Gérer un projet professionnel'), ('BI', 'Développer une solution BI 2'), ('HD', 'Assurer la haute disponibilité'), ('Exploitation', 'Exploitation de données'), ('Admin_SRV', 'Administrer un serveur'), ('Conception DB', 'Conception de Bases de données')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='UniteEnseignement',
        ),
    ]
