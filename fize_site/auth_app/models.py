from django.db import models # type: ignore
from django import forms # type: ignore
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    filiere = models.CharField(max_length=100, blank=True, null=True)
    metier = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    
    first_name = models.CharField(max_length=50)
    
    last_name = models.CharField(max_length=50)
    
    profession = models.CharField(max_length=100, blank=True, null=True)
    
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class StudentForm(forms.ModelForm): # type: ignore
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'filiere','metier', 'photo']
