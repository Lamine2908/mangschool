# Generated by Django 5.0.7 on 2024-10-11 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0164_remove_teacher_classes_remove_classe_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='auth_app.classe'),
        ),
        migrations.AlterField(
            model_name='classe',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='auth_app.teacher'),
        ),
        migrations.RemoveField(
            model_name='matiere',
            name='teacher',
        ),
        migrations.AddField(
            model_name='matiere',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.teacher'),
        ),
    ]
