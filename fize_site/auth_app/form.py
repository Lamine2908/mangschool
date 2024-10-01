from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Note, Paiement, CahierDeCours, Classe, Salle, Comptable, Teacher, Planning,ResponsableClasse, ResponsableFiliere, CahierDeCours
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  
        fields = ('username', 'email')

class ConnexionForm(forms.Form):
    first_name = forms.CharField(
        label="Prénom", 
        max_length=15, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre prénom'
        })
    )
    last_name = forms.CharField(
        label="Nom de famille", 
        max_length=15, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom de famille'
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
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')

        if not first_name or not last_name or not email:
            raise forms.ValidationError("Tous les champs doivent être remplis.")

        return cleaned_data

from django import forms
from .models import Student, Filiere

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'filiere', 'classe', 'metier', 'email']
        widgets = {
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
        fields = ['id', 'first_name', 'last_name', 'profession','email']

class ResponsableClasseForm(forms.ModelForm):
    class Meta:
        model = ResponsableClasse
        fields = ['id', 'first_name', 'last_name','email']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'profession', 'email']

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'profession', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le prénom du prof'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le nom de famille du prof'
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
    
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        profession = cleaned_data.get('profession')
        email = cleaned_data.get('email')

        if not first_name or not last_name or not profession or not email:
            raise forms.ValidationError("Tous les champs obligatoires doivent être remplis.")

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'filiere', 'metier', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom de l\'élève'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de famille de l\'élève'}),
            'filiere': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sélectionnez la filière'}),
            'metier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le métier'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'email de l\'élève'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        filiere = cleaned_data.get('filiere')
        metier = cleaned_data.get('metier')
        email = cleaned_data.get('email')

        if not first_name or not last_name or not filiere  or not metier or not email:
            raise forms.ValidationError("Tous les champs obligatoires doivent être remplis.")

        return cleaned_data

class CahierDeCoursForm(forms.ModelForm):
    class Meta:
        model = CahierDeCours
        fields = ['teacher', 'classe', 'date', 'horaire', 'duree', 'competence', 'uea', 'elements_constituifs',
                'duree_theorie', 'corpus_theorie', 'duree_td', 'corpus_td', 'duree_tp',
                'corpus_tp', 'duree_tpa', 'corpus_tpa', 'duree_stage', 'corpus_stage']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'horaire': forms.TimeInput(attrs={'type': 'time'}),
        }
    
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
        widgets = {
            'salle': forms.CheckboxSelectMultiple(),
            'teacher': forms.CheckboxSelectMultiple(),
            'students': forms.CheckboxSelectMultiple(),
            'matiere': forms.CheckboxSelectMultiple(),
        }
    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['student', 'teacher', 'matiere','note_eva1', 'note_eva2', 'integration','moyen_semes', 'moyen_annuel', 'appreciation']

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
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
        
class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ['date', 'premiere_heure', 'deuxieme_heure', 'troisieme_heure', 'activite1', 'activite2', 'activite3', 'salle', 'professeur']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'premiere_heure': forms.TimeInput(attrs={'type': 'time'}),
            'deuxieme_heure': forms.TimeInput(attrs={'type': 'time'}),
            'troisieme_heure': forms.TimeInput(attrs={'type': 'time'}),
            'activite1': forms.TextInput(attrs={'class': 'form-control'}),
            'activite2': forms.TextInput(attrs={'class': 'form-control'}),
            'activite3': forms.TextInput(attrs={'class': 'form-control'}),
            'salle': forms.Select(attrs={'class': 'form-control'}),
            'professeurs': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class ComptableForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(), required=False, label="Professeurs payés")
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False, label="Étudiants validés")

    class Meta:
        model = Comptable
        fields = ['first_name', 'last_name', 'email', 'teachers', 'students']
        
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

class AddStudentToClassForm(forms.Form):
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), label="Classe")
    student = forms.ModelChoiceField(queryset=Student.objects.filter(classe__isnull=True), label="Étudiant")

    def save(self):
        classe = self.cleaned_data['classe']
        student = self.cleaned_data['student']
        classe.students.add(student)
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
    
class AssignClassToTeacherForm(forms.ModelForm):
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
        fields = ['code_matiere', 'nom_matiere', 'ue', 'credit', 'volume', 'semestre', 'filiere', 'teacher']
