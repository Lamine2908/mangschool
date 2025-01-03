# Generated by Django 5.1.4 on 2025-01-02 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0018_student_date_naissance_alter_student_nin'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjointclasse',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='comptable',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='responsableclasse',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='responsablefiliere',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='responsablemetier',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='mot_de_passe',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
