# Generated by Django 5.1.3 on 2024-11-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0006_alter_matiere_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='volume',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
