# Generated by Django 5.0.7 on 2024-10-17 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_enseigner_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planning',
            name='student',
        ),
        migrations.CreateModel(
            name='Consulter_planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planning', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.planning')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.student')),
            ],
        ),
    ]
