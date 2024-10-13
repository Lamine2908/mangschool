from django.core.management.base import BaseCommand
from auth_app.models import Student, Teacher, Administrateur  # Ajoutez Administrateur ici
import qrcode
from django.core.files import File
from io import BytesIO

class Command(BaseCommand):
    help = 'Génère des codes QR pour les étudiants, enseignants et administrateurs sans code QR'

    def handle(self, *args, **kwargs):
        students_without_qr = Student.objects.filter(qr_code__isnull=True)
        for student in students_without_qr:
            qr_image = qrcode.make(student.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            qr_file_name = f'{student.first_name}_{student.last_name}_qr.png'
            student.qr_code.save(qr_file_name, File(qr_offset), save=True)
            student.save()

        self.stdout.write(self.style.SUCCESS(f'Généré des codes QR pour {students_without_qr.count()} étudiants.'))

        teachers_without_qr = Teacher.objects.filter(qr_code__isnull=True)
        for teacher in teachers_without_qr:
            qr_image = qrcode.make(teacher.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            qr_file_name = f'{teacher.first_name}_{teacher.last_name}_qr.png'
            teacher.qr_code.save(qr_file_name, File(qr_offset), save=True)
            teacher.save()

        self.stdout.write(self.style.SUCCESS(f'Généré des codes QR pour {teachers_without_qr.count()} enseignants.'))

        administrateurs_without_qr = Administrateur.objects.filter(qr_code__isnull=True)
        for administrateur in administrateurs_without_qr:
            qr_image = qrcode.make(administrateur.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            qr_file_name = f'{administrateur.first_name}_{administrateur.last_name}_qr.png'
            administrateur.qr_code.save(qr_file_name, File(qr_offset), save=True)
            administrateur.save()

        self.stdout.write(self.style.SUCCESS(f'Généré des codes QR pour {administrateurs_without_qr.count()} administrateurs.'))
