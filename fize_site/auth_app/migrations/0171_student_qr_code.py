# Generated by Django 5.0.7 on 2024-10-13 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0170_remove_student_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
    ]
