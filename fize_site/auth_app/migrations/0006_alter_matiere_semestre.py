# Generated by Django 5.1.3 on 2024-11-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_matiere_ue_delete_uniteenseignement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='semestre',
            field=models.CharField(choices=[('semes1', 'Semestre 1'), ('semes2', 'Semestre 2'), ('semes3', 'Semestre 3'), ('semes4', 'Semestre 4')], max_length=10, null=True),
        ),
    ]
