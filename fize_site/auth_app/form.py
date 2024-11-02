from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Note, Paiement, CahierDeCours, ResponsableMetier, Projet, Pointage, Classe, Salle, Comptable, Teacher, Planning,ResponsableClasse, ResponsableFiliere, CahierDeCours, Bulletin
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
        fields = ['matricule', 'first_name', 'last_name', 'filiere', 'classe', 'metier', 'email', 'photo']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le matricule'}),            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de famille'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'metier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le métier'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'email'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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
        
class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom', 'responsable']

class ResponsableFiliereForm(forms.ModelForm):
    class Meta:
        model = ResponsableFiliere
        fields = ['matricule', 'first_name', 'last_name', 'profession', 'email', 'num_tel', 'grade']

class ResponsableUpdateForm(forms.ModelForm):
    class Meta:
        model = ResponsableFiliere
        fields = ['matricule', 'first_name', 'last_name', 'profession', 'email', 'num_tel', 'grade']

    def clean(self):
        cleaned_data = super().clean()

        matricule = cleaned_data.get('matricule')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        profession = cleaned_data.get('profession')
        grade = cleaned_data.get('grade')
        email = cleaned_data.get('email')
        num_tel = cleaned_data.get('num_tel')

        if not matricule or not first_name or not last_name or not profession or not grade or not email or not num_tel:
            raise forms.ValidationError("Tous les champs obligatoires doivent être remplis.")

        return cleaned_data

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
        fields = ['matricule', 'first_name', 'last_name', 'filiere', 'metier', 'classe', 'email', 'photo']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le matricule'}),                       
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom de l\'élève'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de famille de l\'élève'}),
            'filiere': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sélectionnez la filière'}),
            'classe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Entrez le classe'}),
            'metier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le métier'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'email de l\'élève'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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

from django import forms
from django.core.exceptions import ValidationError

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['student', 'matiere', 'note_eva1', 'note_eva2', 'integration']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'matiere': forms.Select(attrs={'class': 'form-control'}),
            'note_eva1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note évaluation 1'}),
            'note_eva2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note évaluation 2'}),
            'integration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Intégration'}),
        }

    def __init__(self, *args, valid_classes=None, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.valid_classes = valid_classes  # Liste des classes valides

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_student(self):
        student = self.cleaned_data.get('student')
        if self.valid_classes and student.classe not in self.valid_classes:
            raise ValidationError(f"L'étudiant {student} ne fait pas partie de la classe sélectionnée.")

        return student

class ModifierNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_eva1', 'note_eva2', 'integration']
        widgets = {
            
            'note_eva1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note évaluation 1'}),
            'note_eva2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note évaluation 2'}),
            'integration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Intégration'}),
        }

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
        fields = ['numero', 'name']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de la salle'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la salle'}),
        }
        
class PointageForm(forms.ModelForm):
    class Meta:
        model = Pointage
        fields = ['teacher','student', 'date', 'arrivee', 'sortie']
        widgets = {
            'arrivee': forms.HiddenInput(),
            'sortie': forms.HiddenInput(),
        }

            
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
            'professeur': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
        }

class EditPlanningForm(forms.ModelForm):
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
            'professeur': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
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
        fields = ['classe'] 
    
    def save(self, commit=True):
        student = super().save(commit=False)
        classe = self.cleaned_data['classe']
        student.classe = classe
        if commit:
            student.save()
        return student

from django import forms
from .models import Enseigner, Classe, Matiere

class AffecterProfesseurForm(forms.ModelForm):
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), label="Classe")
    matiere = forms.ModelChoiceField(queryset=Matiere.objects.all(), label="Matière")

    class Meta:
        model = Enseigner
        fields = ['teacher', 'classe', 'matiere']


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
        fields = ['code_matiere', 'nom_matiere', 'ue', 'credit', 'volume', 'semestre', 'filiere', 'teacher', 'responsable']
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
        }
    
    def __init__(self, *args, **kwargs):
        super(MatiereForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})



class ImageUploadForm(forms.Form):
    image = forms.ImageField()

from django import forms
from .models import Media, Enseigner, Classe, Matiere

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title','file']

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super(MediaForm, self).__init__(*args, **kwargs)
        
        if teacher:
            enseignements = Enseigner.objects.filter(matiere__teacher=teacher)
            
            self.fields['classe'] = forms.ModelChoiceField(
                queryset=Classe.objects.filter(id__in=enseignements.values_list('classe_id', flat=True)),
                widget=forms.Select(attrs={'class': 'form-control'}),
                label="Classe"
            )
            self.fields['matiere'] = forms.ModelChoiceField(
                queryset=Matiere.objects.filter(id__in=enseignements.values_list('matiere_id', flat=True)),
                widget=forms.Select(attrs={'class': 'form-control'}),
                label="Matière"
            )

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class ProjetForm(forms.Form):
    class Meta :
        Model = Projet
        field = ['libelle', 'description', 'date', 'student']
        
class ResponsableMetierForm(forms.Form):
    class Meta :
        Model = ResponsableMetier
        field = ['matricule', 'first_name', 'last_name', 'profession', 'status', 'email', 'num_tel'] 