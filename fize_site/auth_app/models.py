import time
from django.db import models
from django.utils import timezone
from django import forms
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import time

class Administrateur(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20 ,unique=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100, default="adresse")
    telephone = models.IntegerField(unique=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    qr_code = models.ImageField(upload_to='qr_codes/students', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/admin', blank=True, null=True)  
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_image = qrcode.make(self.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            self.qr_code.save(f'{self.first_name}_{self.last_name}_qr.png', File(qr_offset), save=False)
        super().save(*args, **kwargs)
            
    def generate_qr_code_data(self):
        return f'{self.id}-{self.first_name}-{self.last_name}'
    
class Salle(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.numero}"

class ResponsableFiliere(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, default='modifier')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    num_tel = models.IntegerField(unique=True, null=True)
    grade = models.CharField(max_length=20, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/students', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/responsable', blank=True, null=True)  
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_image = qrcode.make(self.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            self.qr_code.save(f'{self.first_name}_{self.last_name}_qr.png', File(qr_offset), save=False)
        super().save(*args, **kwargs)
            
    def generate_qr_code_data(self):
        return f'{self.id}-{self.first_name}-{self.last_name}'
    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    matricule = models.CharField(max_length=20, default='matricule')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    num_tel = models.IntegerField(unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True, blank=True)
    comptable = models.ForeignKey('Comptable', on_delete=models.CASCADE, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/teacher', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
     
    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_image = qrcode.make(self.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            self.qr_code.save(f'{self.first_name}_{self.last_name}_qr.png', File(qr_offset), save=False)
        super().save(*args, **kwargs)

    def generate_qr_code_data(self):
        return f'{self.id}-{self.first_name}-{self.last_name}'
    
class Filiere(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nom = models.CharField(max_length=100)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom

class Associer(models.Model): #Filiere
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    
    def __srt__(self):
        return f'{self.teacher}'

class Matiere(models.Model):
    id = models.AutoField(primary_key=True)
    code_matiere = models.CharField(max_length=20, unique=True)
    nom_matiere = models.CharField(max_length=100)
    ue = models.CharField(max_length=100, default='ue')
    credit = models.IntegerField(default=0)
    volume = models.CharField(max_length=5, default='0')
    semestre = models.CharField(max_length=10, default='semestre')
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='matieres', null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.nom_matiere}'
    

class ResponsableMetier(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    matricule = models.CharField(max_length=20, default='matricule')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    num_tel = models.IntegerField(unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.first_name} : {self.last_name}'

class Classe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    promo = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, null=True)
    responsableMetier = models.ForeignKey(ResponsableMetier, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name}-P{self.promo}'

class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    matricule = models.CharField(max_length=20, default='modifier')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True, blank=True)
    metier = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/students', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_image = qrcode.make(self.generate_qr_code_data())
            qr_offset = BytesIO()
            qr_image.save(qr_offset, format='PNG')
            self.qr_code.save(f'{self.first_name}_{self.last_name}_qr.png', File(qr_offset), save=False)
        super().save(*args, **kwargs)
            
    def generate_qr_code_data(self):
        return f'{self.id}-{self.first_name}-{self.last_name}'
    
class Pointage(models.Model):    
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(default=timezone.now)
    arrivee = models.TimeField(default=timezone.now)
    sortie = models.TimeField(default=timezone.now)
    total = models.IntegerField(default=0, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.student}'
    
class Note(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE, null=True, blank=True)
    responsableFiliere = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True, blank=True)    
    note_eva1 = models.FloatField(default=0)
    note_eva2 = models.FloatField(default=0)
    integration = models.FloatField(default=0)
    moyen_semes = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student} - {self.matiere}"

    def save(self, *args, **kwargs):
        self.moyen_semes = round((self.note_eva1 + self.note_eva2 + self.integration) / 3, 2)
        super(Note, self).save(*args, **kwargs)
        
     # def save(self, *args, **kwargs):
    #     if self.matiere not in self.teacher.matieres.all():
    #         raise ValidationError("Le professeur ne peut pas saisir de note pour cette matière.")
    

class Bulletin(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True)
    moyen_semes1 = models.FloatField(default=0)
    moyen_semes2 = models.FloatField(default=0)
    moyen_semes3 = models.FloatField(default=0)
    moyen_semes4 = models.FloatField(default=0)
    moyen_annuel = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.student}'
    
    
    def save(self, *args, **kwargs):
        self.moyen_annuel=(self.moyen_semes1 + self.moyen_semes2 + self.moyen_semes3 + self.moyen_semes4)/4
        super(Note, self).save(*args, **kwargs)

class Enseigner(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='enseignements', null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='enseignements', null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, related_name='students')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='classes')
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, related_name='enseignements', null=True)
    
    def __str__(self):
        return f"{self.teacher} enseigne {self.matiere} dans {self.classe}"
    
class Programme(models.Model):
    code_programme = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    responsablefiliere = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE)

MOYENS_PAIEMENT = [('CB', 'Carte Bancaire'), ('PP', 'Paypal'), ('BT', 'Virement Bancaire'),]

class Paiement(models.Model):   
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    moyen_paiement = models.CharField(max_length=10, choices=MOYENS_PAIEMENT, default='CB')
    est_paye = models.BooleanField(default=False)

    def __str__(self):
        return f"Paiement de {self.student} pour {self.montant} F CFA"


class Comptable(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, default='modifier')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Oberver_paiement(models.Model):
    comptable = models.ForeignKey(Comptable, on_delete=models.CASCADE, null=True)
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.comptable}'

class ResponsableClasse(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, default='modifier')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class AdjointClasse(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, default='modifier')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CahierDeCours(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(default=timezone.now)
    horaire = models.CharField(max_length=35, null=True)
    duree = models.CharField(max_length=5, null=True)
    competence = models.CharField(max_length=100)
    uea = models.CharField(max_length=5, null=True)
    elements_constituifs = models.TextField(max_length=50)
    duree_theorie = models.CharField(max_length=5, null=True)
    corpus_theorie = models.TextField(blank=True, null=True)
    duree_td = models.CharField(max_length=5, null=True)
    corpus_td = models.TextField(blank=True, null=True)
    duree_tp = models.CharField(max_length=5, null=True)
    corpus_tp = models.TextField(blank=True, null=True)
    duree_tpa = models.CharField(max_length=5, null=True)
    corpus_tpa = models.TextField(blank=True, null=True)
    duree_stage = models.CharField(max_length=5, null=True)
    corpus_stage = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableClasse, on_delete=models.CASCADE, null=True)
    adjoint = models.ForeignKey(AdjointClasse, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'Cahier de {self.teacher} pour la classe {self.classe} le {self.date}'

class Planning(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(default=timezone.now)
    premiere_heure = models.TimeField(default='08:30')
    deuxieme_heure = models.TimeField(default='11:00')
    troisieme_heure = models.TimeField(default='14:00')
    activite1 = models.CharField(max_length=100, null=True)
    activite2 = models.CharField(max_length=100, null=True)
    activite3 = models.CharField(max_length=100, null=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    professeur = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.date})"

class Consulter_planning(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, null=True)
    
MEDIA_TYPE_CHOICES = [
        ('book', 'Livre'),
        ('pdf', 'PDF'),
        ('video', 'Vidéo'),
    ]
class Media(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, null=True)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Projet(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    libelle=models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='media/projet', null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, null=True)    
    date = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.libelle}'