# Generated by Django 5.1.1 on 2025-01-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0027_alter_administrateur_qr_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Projects\\essai\x0cize_site\\qr_codes\\student'),
        ),
    ]
