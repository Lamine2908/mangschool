# Generated by Django 5.0.7 on 2024-10-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0156_alter_cahierdecours_horaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='horaire',
            field=models.CharField(max_length=15),
        ),
    ]
