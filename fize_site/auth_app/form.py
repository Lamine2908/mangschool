from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Note, Paiement, CahierDeCours, Pointage, Classe, Salle, Comptable, Teacher, Planning,ResponsableClasse, ResponsableFiliere, CahierDeCours, Bulletin
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  
        fields = ('username', 'email')

class ConnexionForm(forms.Form):
    matricule = forms.CharField(
        label="Matricule", 
        max_length=15, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre matricule'
        })
    )
    email = forms.EmailField(
        label="EMAIL", 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre email'
        })
    )
   

    def clean(self):
        cleaned_data = super().clean()
        
        matricule = cleaned_data.get('matricule')
        email = cleaned_data.get('email')
        
        if not matricule or not email :
            raise forms.ValidationError("Veuillez reessayer.")

        return cleaned_data

from django import forms
from .models import Student, Filiere

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matricule', 'first_name', 'last_name', 'filiere', 'classe', 'metier', 'email']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le matricule'}),            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de famille'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'metier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le métier'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'email'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['filiere'].queryset = Filiere.objects.all()
        self.fields['classe'].queryset = Classe.objects.all()
        
class ResponsableFiliereForm(forms.ModelForm):
    class Meta:
        model = ResponsableFiliere
        fields = ['matricule', 'first_name', 'last_name', 'profession','email']

class ResponsableClasseForm(forms.ModelForm):
    class Meta:
        model = ResponsableClasse
        fields = ['matricule', 'first_name', 'last_name','email']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['matricule', 'first_name', 'last_name', 'profession', 'email']

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['matricule', 'first_name', 'last_name', 'profession', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le prénom du prof'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le nom de famille du prof'
            }),
             'matricule': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le matricule du prof'
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sélectionnez la profession'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez l\'email du prof'
            }),
        }


    def clean(self):
        cleaned_data = super().clean()

        matricule = cleaned_data.get('matricule')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        profession = cleaned_data.get('profession')
        email = cleaned_data.get('email')

        if not matricule or not first_name or not last_name or not profession or not email:
            raise forms.ValidationError("Tous les champs obligatoires doivent être remplis.")

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matricule', 'first_name', 'last_name', 'filiere', 'metier', 'classe', 'email']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le matricule'}),                       
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom de l\'élève'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de famille de l\'élève'}),
            'filiere': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sélectionnez la filière'}),
            'classe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Entrez le classe'}),
            'metier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le métier'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'email de l\'élève'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        matricule = cleaned_data.get('matricule')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        filiere = cleaned_data.get('filiere')
        metier = cleaned_data.get('metier')
        email = cleaned_data.get('email')

        if not matricule or not first_name or not last_name or not filiere  or not metier or not email:
            raise forms.ValidationError("Tous les champs obligatoires doivent être remplis.")

        return cleaned_data



class CahierDeCoursForm(forms.ModelForm):
    classe = forms.ModelChoiceField(
        queryset=Classe.objects.all(),
        required=True,
        label="Classe",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CahierDeCours
        fields = ['date', 'classe', 'horaire', 'duree', 'competence', 'uea', 'elements_constituifs', 
                  'duree_theorie', 'corpus_theorie', 'duree_td', 'corpus_td', 
                  'duree_tp', 'corpus_tp', 'duree_tpa', 'corpus_tpa']


class CahierFilterForm(forms.Form):
    classe = forms.ModelChoiceField(
        queryset=Classe.objects.all(),
        required=False,
        label="Classe",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateField(
        required=False,
        label="Date",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

        

        
class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['moyen_paiement', 'montant', 'student']

    def clean(self):
        cleaned_data = super().clean()
        student = self.cleaned_data.get('student')

        if Paiement.objects.filter(student=student, est_paye=True).exists():
            raise forms.ValidationError("Vous avez déjà effectué un paiement.")
        return cleaned_data
    
class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['classe','student', 'matiere', 'note_eva1', 'note_eva2', 'integration']
        widgets = {
            'classe': forms.Select(attrs={'class': 'form-control'}),            
            'student': forms.Select(attrs={'class': 'form-control'}),
            'matiere': forms.Select(attrs={'class': 'form-control'}),
            'note_eva1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note évaluation 1'}),
            'note_eva2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note évaluation 2'}),
            'integration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Intégration'}),
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
    
    

class BulletinForm(forms.Form):
    class Meta:
        model = Bulletin
        fields = '__all__'
 
    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'}) 
            
class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['code','numero', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code de la salle'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de la salle'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la salle'}),
        }
        
class PointageForm(forms.ModelForm):
    class Meta:
        model = Pointage
        fields = ['student', 'arrivee', 'sortie']
        widgets = {
            'arrivee': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'sortie': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PointageForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

            
class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'premiere_heure': forms.TimeInput(attrs={'type': 'time'}),
            'deuxieme_heure': forms.TimeInput(attrs={'type': 'time'}),
            'troisieme_heure': forms.TimeInput(attrs={'type': 'time'}),
            'activite1': forms.TextInput(attrs={'class': 'form-control'}),
            'activite2': forms.TextInput(attrs={'class': 'form-control'}),
            'activite3': forms.TextInput(attrs={'class': 'form-control'}),
            'salle': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'professeur': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComptableForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(), required=False, label="Professeurs payés")
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False, label="Étudiants validés")

    class Meta:
        model = Comptable
        fields = ['matricule','first_name', 'last_name', 'email', 'teachers', 'students']
        
# class ValidatePaymentForm(forms.ModelForm):
#     class Meta:
#         model = TeacherPayment
#         fields = ']
        
# class TeacherPaymentForm(forms.ModelForm):
#     class Meta:
#         model = TeacherPayment
#         fields = ['amount']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['amount'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Entrez le montant'})


class AffecterEleveForm(forms.ModelForm):
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), label="Classe")

    class Meta:
        model = Student
        fields = ['classe']  # Spécifiez les champs de votre modèle
    
    def save(self, commit=True):
        student = super().save(commit=False)
        classe = self.cleaned_data['classe']
        student.classe = classe
        if commit:
            student.save()
        return student

class AssignClassForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['classe']
        labels = {
            'classe': 'Sélectionner la Classe',
        }
        widgets = {
            'classe': forms.Select(attrs={'class': 'form-control'}),
        }
    
class AffecterProfForm(forms.ModelForm):
    classes = forms.ModelMultipleChoiceField(
        queryset=Classe.objects.all(),
        widget=forms.CheckboxSelectMultiple, 
        required=True
    )

    class Meta:
        model = Teacher
        fields = ['classes']
        
class AssignStudentToClassForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['classe']
        widgets = {
            'classe': forms.Select(attrs={'class': 'form-control'}),
        }
              
class ClassInfoForm(forms.Form):
    classe = forms.ModelChoiceField(
        queryset=Classe.objects.all(),
        label="Choisissez une classe",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
from .models import Matiere

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['code_matiere', 'nom_matiere', 'ue', 'credit', 'volume', 'semestre', 'filiere', 'teacher', 'responsable', 'classes']
        widgets = {
            'code_matiere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code de la matière'}),
            'nom_matiere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la matière'}),
            'ue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unité d\'enseignement'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Crédits'}),
            'volume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Volume horaire'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Semestre'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(MatiereForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})



class ImageUploadForm(forms.Form):
    image = forms.ImageField()