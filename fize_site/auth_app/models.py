import time
from django.db import models
from django.utils import timezone
from django import forms
import qrcode
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User

class Administrateur(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20 ,unique=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100, default="adresse")
    telephone = models.IntegerField(unique=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

class Salle(models.Model):
    code = models.CharField(max_length=10, unique=True, null=True, blank=True)  
    numero = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    classes = models.ManyToManyField('Classe', related_name='teachers')
    matieres = models.ManyToManyField('Matiere', related_name='matiere')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ResponsableFiliere(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Filiere(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nom = models.CharField(max_length=100)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

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
    
    def __str__(self):
        return self.nom_matiere

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True, blank=True)
    matiere = models.ManyToManyField(Matiere, related_name='students')
    metier = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    classe = models.ForeignKey('Classe', related_name='students_in', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Classe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    salle = models.ManyToManyField(Salle, related_name='classes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='classes')
    matiere = models.ManyToManyField(Matiere, related_name='classes')
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='classes', null=True)


    def __str__(self):
        return self.name

class Note(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='notes')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True, related_name='matieres')
    administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE, null=True)
    note_eva1 = models.FloatField(default=0)
    note_eva2 = models.FloatField(default=0)
    integration = models.FloatField(default=0)
    moyen_semes = models.FloatField(default=0)
    moyen_annuel = models.FloatField(default=0)
    appreciation = models.CharField(max_length=15, default='pas encore', blank=True)
    
    def __str__(self):
        return f"{self.student} - {self.moyen_semes}"

    def save(self, *args, **kwargs):
        self.moyen_semes = (self.note_eva1 + self.note_eva2 + self.integration) / 3
        super(Note, self).save(*args, **kwargs)

class Enseigner(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('teacher', 'matiere', 'classe', 'salle')

class Programme(models.Model):
    code_programme = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    responsablefiliere = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE)

class Planifier(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    filiere = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE)

class Paiement(models.Model):
    MOYENS_PAIEMENT = [
        ('CB', 'Carte Bancaire'),
        ('PP', 'Paypal'),
        ('BT', 'Virement Bancaire'),
    ]
    
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    comptable = models.ForeignKey('Comptable', on_delete=models.SET_NULL, null=True, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    moyen_paiement = models.CharField(max_length=2, choices=MOYENS_PAIEMENT, default='CB')
    est_paye = models.BooleanField(default=False)

    def __str__(self):
        return f"Paiement de {self.student} pour {self.montant} €"


class Comptable(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    teachers = models.ManyToManyField('Teacher', related_name='comptable_paye', blank=True)
    students = models.ManyToManyField('Student', related_name='comptable_valide', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ResponsableClasse(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class AdjointClasse(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CahierDeCours(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='cahiers')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, related_name='cahiers')
    date = models.DateField()
    horaire = models.CharField(max_length=20)
    duree = models.CharField(max_length=50)
    competence = models.CharField(max_length=100)
    uea = models.CharField(max_length=100)
    elements_constituifs = models.TextField()
    duree_theorie = models.CharField(max_length=50, blank=True, null=True)
    corpus_theorie = models.TextField(blank=True, null=True)
    duree_td = models.CharField(max_length=50, blank=True, null=True)
    corpus_td = models.TextField(blank=True, null=True)
    duree_tp = models.CharField(max_length=50, blank=True, null=True)
    corpus_tp = models.TextField(blank=True, null=True)
    duree_tpa = models.CharField(max_length=50, blank=True, null=True)
    corpus_tpa = models.TextField(blank=True, null=True)
    duree_stage = models.CharField(max_length=50, blank=True, null=True)
    corpus_stage = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('teacher', 'classe', 'date')

    def __str__(self):
        return f'Cahier de {self.teacher} pour la classe {self.classe} le {self.date}'

class Planning(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=timezone.now)
    premiere_heure = models.TimeField()
    deuxieme_heure = models.TimeField()
    troisieme_heure = models.TimeField(default='00:00')
    activite1 = models.CharField(max_length=100)
    activite2 = models.CharField(max_length=100, default='Activite2')
    activite3 = models.CharField(max_length=100, default='Activite3')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, default=1)
    professeur = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.activite1} - {self.activite2} - {self.date} ({self.premiere_heure} - {self.deuxieme_heure} - {self.troisieme_heure})"

# class TeacherPayment(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     montant = models.DecimalField(max_digits=10, decimal_places=2, default=120.00)  # Montant par défaut fixé à 120 euros
#     payee = models.BooleanField(default=False)
#     payment_date = models.DateField(null=True, blank=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

#     def mark_payee(self):
#         self.payee = True
#         self.payment_date = timezone.now()
#         self.save()