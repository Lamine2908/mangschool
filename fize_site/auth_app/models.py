import time
from django.db import models
from django.utils import timezone
from django import forms
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import time, timedelta, datetime
import uuid,random, string
from django.db import IntegrityError

def generate_unique_matricule():
       return ''.join(random.choices(string.ascii_letters + string.digits, k=10)).upper()

class Administrateur(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100, default="adresse")
    telephone = models.IntegerField(unique=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    qr_code = models.ImageField(upload_to='qr_codes/student', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/admin', blank=True, null=True)  
    mot_de_passe = models.CharField(max_length=50, null=True)
    
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
    
    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(Administrateur, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(Administrateur, self).save(*args, **kwargs)

salle = [
    ('310', '310'), ('311', '311'), ('312', '312'), ('313', '313'), ('314', '314')
]

filiere = [
    ('Mécanique', 'Mecanique'),
    ('TIC', 'TIC')
]

class ResponsableFiliere(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    num_tel = models.IntegerField(unique=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/responsable', blank=True, null=True)
    office = models.CharField(max_length=20, null=True)
    prise_de_fonction = models.DateField(null=True)
    photo = models.ImageField(upload_to='photos/responsable', blank=True, null=True)  
    mot_de_passe = models.CharField(max_length=50, null=True) 
    
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
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField( null=True, blank=True)
    num_tel = models.IntegerField(unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True, blank=True)
    comptable = models.ForeignKey('Comptable', on_delete=models.CASCADE, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/teacher', blank=True, null=True)
    mot_de_passe = models.CharField(max_length=50, null=True)
    
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
    
    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(Teacher, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(Teacher, self).save(*args, **kwargs)

class Filiere(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nom = models.CharField(max_length=100, choices=filiere, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom

class Associer(models.Model): #Filiere
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    
    def __srt__(self):
        return f'{self.teacher}'

UniteEnseignement = [
    ('Appliquer les bases en informatique', 'Appliquer les bases en informatique'),
    ('Initialisation au Génie Logiciel', 'Initialisation au Génie Logiciel'),
    ('Découvrir le milieu professionnel', 'Découvrir le milieu professionnel'),
    ('bases en mathématiques', 'bases en mathématiques'),
    ('Gérer un projet professionnel', 'Gérer un projet professionnel'),
    ('évelopper une solution BI', 'Développer une solution BI'),
    ('Assurer la haute disponibilité', 'Assurer la haute disponibilité'),
    ('Exploitation de données', 'Exploitation de données'),
    ('Administrer un serveur', 'Administrer un serveur'),
    ('Conception de Bases de données', 'Conception de Bases de données')
]

semestres = [
    ('Semestre 1', 'Semestre 1'),
    ('Semestre 2', 'Semestre 2'),
    ('Semestre 3', 'Semestre 3'),
    ('Semestre 4', 'Semestre 4'),
]
    
class Matiere(models.Model):
    id = models.AutoField(primary_key=True)
    code_matiere = models.CharField(max_length=20, unique=True)
    nom_matiere = models.CharField(max_length=100)
    credit = models.IntegerField(default=0, null=True, blank=True)
    volume = models.IntegerField(default=0, null=True)
    semestre = models.CharField(max_length=10, choices=semestres, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='matieres',  choices=filiere, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    ue = models.CharField(max_length=100, choices=UniteEnseignement ,null=True)

    def __str__(self):
        return f'{self.nom_matiere}'
    
    def save(self, *args, **kwargs):
        self.volume = self.credit * 20
        super(Matiere, self).save(*args, **kwargs)  

class ResponsableMetier(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    num_tel = models.IntegerField(unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    administrateur=models.ForeignKey(Administrateur, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    mot_de_passe = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(ResponsableMetier, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(ResponsableMetier, self).save(*args, **kwargs)

class Classe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    promo = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, null=True)
    responsableMetier = models.ForeignKey(ResponsableMetier, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name}-P{self.promo}'

METIER_TYPE_CHOICES = [
    ('Administration de bases de données', 'Administration de bases de données'),
    ('Analyse de performance digitale', 'Analyse de performance digitale'),
    ('Développement Front-End', 'Développement Front-End'),
    ('Développement Back-End', 'Développement Back-End'),
    ('Système, sécurité et cloud', 'Système, sécurité et cloud'),
    ('Réseau et Internet des objets', 'Réseau et Internet des objets'),
]

class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_naissance = models.DateField(null=True)
    lieu_naissance = models.CharField(max_length=50, null=True)
    nin = models.IntegerField(null=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True, blank=True)
    metier = models.CharField(
        max_length=50, 
        choices=METIER_TYPE_CHOICES, 
        null=True, 
        blank=True
    )
    email = models.EmailField( null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/student', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    mot_de_passe = models.CharField(max_length=50, null=True)
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
    
    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(Student, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(Student, self).save(*args, **kwargs)

class Pointage(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(default=timezone.now)
    arrivee = models.TimeField(null=True, blank=True)  
    sortie = models.TimeField(null=True, blank=True) 
    total = models.DurationField(default=timedelta(0), null=True, blank=True) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)

    def calculer_total(self):
        if self.arrivee and self.sortie:
            arrivee_datetime = datetime.combine(self.date, self.arrivee)
            sortie_datetime = datetime.combine(self.date, self.sortie)
            self.total = sortie_datetime - arrivee_datetime
        else:
            self.total = timedelta(0)

    def save(self, *args, **kwargs):
        self.calculer_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.date}"

    
class Note(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)    
    note_eva1 = models.FloatField(default=0)
    note_eva2 = models.FloatField(default=0)
    integration = models.FloatField(default=0)
    moyen_semes = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student} - {self.matiere}"

    def save(self, *args, **kwargs): 
        if self.student.classe != self.classe: 
            raise ValidationError(f"L'élève {self.student} n'appartient pas à la classe {self.classe}.")

    def save(self, *args, **kwargs):
        self.moyen_semes = round((self.note_eva1 + self.note_eva2 + self.integration) / 3, 2)
        super(Note, self).save(*args, **kwargs)

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
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(Comptable, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(Comptable, self).save(*args, **kwargs)

class Oberver_paiement(models.Model):
    comptable = models.ForeignKey(Comptable, on_delete=models.CASCADE, null=True)
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.comptable}'

class ResponsableClasse(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    mot_de_passe = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(ResponsableClasse, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(ResponsableClasse, self).save(*args, **kwargs)

class AdjointClasse(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, unique=True, default=generate_unique_matricule, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    mot_de_passe = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
       if not self.matricule:
           self.matricule = generate_unique_matricule()
       try:
           super(AdjointClasse, self).save(*args, **kwargs)
       except IntegrityError:
           self.matricule = generate_unique_matricule()
           super(AdjointClasse, self).save(*args, **kwargs)


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
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)
    adjoint = models.ForeignKey(AdjointClasse, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'Cahier de {self.teacher} pour la classe {self.classe} le {self.date}'

class Planning(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(default=timezone.now)
    premiere_heure = models.TimeField(default='08:30')
    deuxieme_heure = models.TimeField(default='11:00')
    troisieme_heure = models.TimeField(default='14:00')
    matiere=models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True)
    salle = models.CharField(max_length=4,choices=salle, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    professeur = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(ResponsableFiliere, on_delete=models.CASCADE, null=True)

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