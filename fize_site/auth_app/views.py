from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, Classe, Salle, Note, Matiere, CahierDeCours, TeacherPayment, Comptable, Paiement, Administrateur, Planning, ResponsableFiliere, ResponsableClasse
from .form import StudentForm,PaiementForm, NoteForm, MatiereForm, CahierDeCoursForm, ClassInfoForm, TeacherPaymentForm, AssignStudentToClassForm, AssignClassToTeacherForm, AddStudentToClassForm, ComptableForm, ClasseForm, SalleForm, AssignClassForm, TeacherForm, PlanningForm , CustomUserCreationForm, ConnexionForm, ResponsableFiliereForm, TeacherUpdateForm, StudentUpdateForm
from django.core.mail import send_mail
from django.utils import timezone

from django.contrib.auth.decorators import login_required, user_passes_test

def navigation(request):
    return render(request, 'navigation.html')

def espaceeleve(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'espaceeleve.html', {'student': student})

def espaceseleves(request):
    student = Student.objects.all()
    return render(request, 'espaceeleve.html', {'student': student})

def espaceadmin(request, admin_id):
    administrateur = get_object_or_404(Administrateur, id=admin_id)
    return render(request, 'espaceadmin.html', {'administrateur': administrateur})

def espaceadmins(request):
    administrateur = Administrateur.objects.all()
    return render(request, 'espaceadmin.html', {'administrateur': administrateur})

def responsables_filieres(request):
    responsableFilieres = ResponsableFiliere.objects.all()
    return render(request, 'responsable_filiere.html', {'responsableFilieres': responsableFilieres})

def responsable_filiere(request, responsable_id):
    responsableFiliere = get_object_or_404(ResponsableFiliere, id=responsable_id)
    return render(request, 'responsable_filiere.html', {'responsableFiliere': responsableFiliere})

def espaceprof(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'espaceprof.html', {'teacher': teacher})

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def espaceresponsableclasse(request):
    return render(request, 'responsableClasse.html')

def comptable(request):
    return render(request, 'espacecomptable.html')

def responsableclasse(request, responsable_id):
    responsableClasse = get_object_or_404(ResponsableClasse, id=responsable_id)
    return render(request, 'responsableClasse.html', {'responsableClasse': responsableClasse})

def espacecomptable(request, comptable_id):
    comptables = get_object_or_404(Comptable, id=comptable_id)
    return render(request, 'espacecomptable.html', {'comptables': comptables})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            try:
                student = Student.objects.get(first_name=first_name, last_name=last_name, email=email)
                return redirect('espaceeleve', student_id=student.id)
            except Student.DoesNotExist:
                pass

            try:
                teacher = Teacher.objects.get(first_name=first_name, last_name=last_name, email=email)
                return redirect('espaceprof', teacher_id=teacher.id)
            except Teacher.DoesNotExist:
                pass
            
            try:
                administrateur = Administrateur.objects.get(first_name=first_name, last_name=last_name, email=email)
                return redirect('espaceadmin', admin_id=administrateur.id)
            except Administrateur.DoesNotExist:
                pass
            
            try:
                responsableFiliere = ResponsableFiliere.objects.get(first_name=first_name, last_name=last_name, email=email)
                return redirect('responsable_filiere', responsable_id=responsableFiliere.id)
            except ResponsableFiliere.DoesNotExist:
                pass
            
            try:
                comptable = Comptable.objects.get(first_name=first_name, last_name=last_name, email=email)
                return redirect('espacecomptable', comptable_id=comptable.id)
            except Comptable.DoesNotExist:
                pass
            
            try:
                responsableclasse = ResponsableClasse.objects.get(first_name=first_name, last_name=last_name, email=email)
                return redirect('responsableclasse', responsable_id=responsableclasse.id)
            except ResponsableFiliere.DoesNotExist:
                pass
            
            messages.error(request, "L'utilisateur n'existe pas.")

    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', {'form': form})


def index(request):
    return render(request, 'index.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def delete_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "L'élève a été supprimé avec succès.")
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})

def delete_teacher_by_id(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        messages.success(request, "Le professeur a été supprimé avec succès.")
        return redirect('teacher_list')

    return render(request, 'delete_teachers.html', {'teacher': teacher})

def delete_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "L eleve a été supprimé avec succès.")
        return redirect('student_list')

    return render(request, 'delete_students.html', {'student': student})

def success_page(request):
    return render(request, 'success.html')

def filter_students_view(request):
    students = Student.objects.all()

    id = request.GET.get('id')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    if id:
        students = students.filter(id=id)
    elif first_name:
        students = students.filter(first_name__icontains=first_name)
    elif last_name:
        students = students.filter(last_name__icontains=last_name)

    return render(request, 'filter_students.html', {'students': students})

def filter_teacher(request):
    teachers = Teacher.objects.all()
    
    id=request.GET.get('id')
    first_name= request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    
    if id:
        teachers = teachers.filter(id=id)
    elif first_name:
        teachers = teachers.filter(first_name__icontains=first_name)
    elif last_name:
        teachers = teachers.filter(last_name__icontains = last_name)
        
    return render(request, 'filter_teachers.html', {'teachers': teachers})

def update_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherUpdateForm(instance=teacher)
    
    return render(request, 'update_teacher.html', {'form': form, 'teacher': teacher})

def update_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else: 
        student = get_object_or_404(Student, id=student_id)
        form = StudentUpdateForm(request.POST, instance=student)
        
    return render(request, 'update_student.html', {'form': form, 'student': student})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def detail_prof(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def ajouter_matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm()

    return render(request, 'ajouter_matiere.html', {'form': form})


def modifier_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm(instance=matiere)

    return render(request, 'modifier_matiere.html', {'form': form})


def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'liste_matieres.html', {'matieres': matieres})

def supprimer_matiere(request, matiere_id):
    matiere = Matiere.objects.get(id=matiere_id)
    if request.method == 'POST':
        matiere.delete()
        return redirect('liste_matieres')

    return render(request, 'supprimer_matiere.html', {'matiere': matiere})



def paiement_etudiant(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if Paiement.objects.filter(student=student).exists():
        messages.error(request, "Cet étudiant a déjà effectué un paiement.")
        return redirect('paiement_liste')

    if request.method == 'POST':
        form = PaiementForm(request.POST)
        if form.is_valid():
            paiement = form.save(commit=False)
            paiement.student = student
            paiement.save()
            messages.success(request, f"Le paiement a été enregistré avec succès pour l'étudiant {student}.")
            return redirect('paiement_liste') 
    else:
        form = PaiementForm()

    return render(request, 'paiement_etudiant.html', {'form': form, 'student': student})

def valider_paiement(request, paiement_id):
    paiement = get_object_or_404(Paiement, id=paiement_id)
    if hasattr(request.user, 'comptable'): 
        paiement.est_paye = True
        paiement.comptable = request.user.comptable
        paiement.save()
        messages.success(request, f"Le paiement de {paiement.student} a été validé.")
        return redirect('paiement_liste')
    else:
        messages.error(request, "Vous n'êtes pas autorisé à valider les paiements.")
        return redirect('home')

def paiement_liste(request):
    paiements = Paiement.objects.all()
    return render(request, 'paiement_liste.html', {'paiements': paiements})

def ajouter_notes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
   
    classes = Classe.objects.filter(teacher=teacher)
    students = Student.objects.filter(classe__in=classes).distinct()
    matieres = Matiere.objects.filter(classes__in=classes).distinct()
    teachers = Teacher.objects.filter(classe__in=classes).distinct()
    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            existence_note = Note.objects.filter(student=note.student, matiere=note.matiere, teacher=teacher).first()
            
            if existence_note:
                messages.error(request, f"Une note existe déjà pour {note.student} dans {note.matiere}.")
                return redirect('ajouter_notes', teacher_id=teacher_id)   
                 
            note.teacher = teacher
            note.save()
            return redirect('afficher_notes', teacher_id=teacher_id)
    else:
        form = NoteForm()
    context = {
        'teacher': teacher,
        'classes': classes,
        'matieres': matieres,
        'students': students,
        'teachers':teachers,
        'form': form,
    }
    
    return render(request, 'ajouter_notes.html', context)

def afficher_notes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    classes = Classe.objects.filter(teacher=teacher)
    students = Student.objects.filter(classe__in=classes).distinct()
    notes = Note.objects.filter(student__in=students)
    context = {
        'teacher': teacher,
        'classes': classes,
        'students': students,
        'notes': notes,
    }
    
    return render(request, 'afficher_notes.html', context)

def modifier_notes(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('afficher_notes', teacher_id=note.teacher.id)
    else:
        form = NoteForm(instance=note)
    
    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'modifier_notes.html', context)


def ajouter_classe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_classes') 
    else:
        form = ClasseForm()  

    return render(request, 'ajouter_classe.html', {'form': form})

def liste_classes(request):
    classes = Classe.objects.all()
    return render(request, 'liste_classes.html', {'classes': classes})

def prof_etudiant_list(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    classes = Classe.objects.filter(teacher=teacher)
    students = Student.objects.filter(classe__in=classes).distinct()
    context = {
        'teacher': teacher,
        'classes': classes,
        'students': students,
    }
    
    return render(request, 'prof_etudiant_list.html', context)

def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'liste_salles.html', {'salles': salles})

def ajouter_salle(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salle ajoutée avec succès.')
            return redirect('ajouter_salle')
    else:
        form = SalleForm()
    
    return render(request, 'ajouter_salle.html', {'form': form})

def modifier_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == "POST":
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('liste_classes') 
    else:
        form = ClasseForm(instance=classe)
    
    return render(request, 'modifier_classe.html', {'form': form, 'classe': classe})

def supprimer_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == "POST":
        classe.delete()
        return redirect('liste_classes')
    
    return render(request, 'supprimer_classe.html', {'classe': classe})

def ajouter_salle(request):
    if request.method == "POST":
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_salles')
    else:
        form = SalleForm()
    
    return render(request, 'ajouter_salle.html', {'form': form})

def modifier_salle(request, id):
    salle = get_object_or_404(Salle, id=id)
    if request.method == "POST":
        form = SalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save()
            return redirect('liste_salles')
    else:
        form = SalleForm(instance=salle)
    
    return render(request, 'modifier_salle.html', {'form': form, 'salle': salle})

def supprimer_salle(request, id):
    salle = get_object_or_404(Salle, id=id)
    if request.method == "POST":
        salle.delete()
        return redirect('liste_salles')
    
    return render(request, 'supprimer_salle.html', {'salle': salle})

def is_admin(user):
    return user.is_staff 

def comptable_view(request):
    if request.method == 'POST':
        form = ComptableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comptable_detail')
    else:
        form = ComptableForm()

    return render(request, 'comptable_form.html', {'form': form})

def comptable_list(request):
    comptables = Comptable.objects.all()
    return render(request, 'comptable_list.html', {'comptables': comptables})

def comptable_detail(request, id):
    comptable = get_object_or_404(Comptable, id=id)
    return render(request, 'comptable_detail.html', {'comptable': comptable})

def comptable_edit(request, id):
    comptable = get_object_or_404(Comptable, id=id)
    return render(request, 'comptable_edit.html', {'comptable': comptable})

def comptable_delete(request, id):
    comptable = get_object_or_404(Comptable, id=id)
    return redirect('comptable_list', {'comptable': comptable})


def initialize_teacher_payments():
    teachers = Teacher.objects.all()
    for teacher in teachers:
        if not TeacherPayment.objects.filter(teacher=teacher).exists():
            TeacherPayment.objects.create(teacher=teacher, amount=300.000)

def view_teacher_payments(request):
    initialize_teacher_payments()

    payments = TeacherPayment.objects.all()

    if request.method == 'POST':
        payment_id = request.POST.get('payment_id')
        payment = get_object_or_404(TeacherPayment, id=payment_id)
        payment.mark_as_paid()
        return redirect('view_teacher_payments')

    return render(request, 'teacher_payments.html', {'payments': payments})

def manage_payments(request):
    if request.method == 'POST':
        form = TeacherPaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            teacher_id = request.POST.get('teacher_id')
            teacher = get_object_or_404(Teacher, id=teacher_id)
            payment, created = TeacherPayment.objects.get_or_create(teacher=teacher)
            payment.amount = amount
            payment.save()
            return redirect('payment_list')
    else:
        form = TeacherPaymentForm()

    teachers = Teacher.objects.all()
    return render(request, 'manage_payments.html', {'form': form, 'teachers': teachers})

def payment_list(request):
    payments = TeacherPayment.objects.all().order_by('-payment_date')  # Tri des paiements par date
    return render(request, 'payment_list.html', {'payments': payments})

def class_info(request):
    classes = Classe.objects.all()
    teachers = Classe.objects.all()
    students = Classe.objects.count()
    return render(request, 'class_info.html', {
        'classes': classes,
        'teachers': teachers,
        'students':students
    })

def class_list(request):
    classes = Classe.objects.all()
    return render(request, 'class_info.html', {'classes': classes})

def assign_teacher_to_classes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        form = AssignClassToTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_class') 
    else:

        form = AssignClassToTeacherForm(instance=teacher)
    
    return render(request, 'affecter_prof.html', {'form': form, 'teacher': teacher})

def teacher_class(request):

    teachers = Teacher.objects.prefetch_related('classes').all()
    return render(request, 'teacher_classe.html', {'teachers': teachers})

# def assign_student_to_class(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
    
#     if request.method == 'POST':
#         form = AssignStudentToClassForm(request.POST, instance=student)
#         if form.is_valid():
#             if student.classe is not None:
#                 messages.error(request, "Cet étudiant est déjà affecté à une classe.")
#             else:
#                 form.save()
#                 messages.success(request, "L'étudiant a été affecté à la classe avec succès.")
#                 return redirect('class_student_list') 
#     else:
#         form = AssignStudentToClassForm(instance=student)
    
#     return render(request, 'assign_student_to_class.html', {'form': form, 'student': student})

def Affecter_eleve(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = AddStudentToClassForm(request.POST, instance=student)
        if form.is_valid():
            if student.classe is not None:
                return redirect('liste_classe')
            else:
                form.save()
                return redirect('liste_classe')
    else:
        form = AddStudentToClassForm(instance=student)
        
    return render(request, 'affecter_eleve.html', {'form':form, 'student':student})

def liste_classe(request):
    students = Student.objects.filter(classe__isnull=False)
    classes = Classe.objects.prefetch_related('students_in').all()
    return render(request, 'liste_classe.html', {'students': students, 'classes':classes})

def remplir_cahier(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    # Filtrer les classes associées à l'enseignant
    classes = Classe.objects.filter(teacher=teacher)
    
    if request.method == 'POST':
        form = CahierDeCoursForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            
            # Vérifier si un cahier a déjà été rempli à cette date pour cet enseignant
            if CahierDeCours.objects.filter(teacher=teacher, date=date).exists():
                form.add_error(None, "Vous avez déjà rempli un cahier de cours à cette date.")
            else:
                cahier = form.save(commit=False)
                cahier.teacher = teacher
                cahier.save()
                return redirect('liste_cahiers', teacher_id=teacher.id)
        else:
            print(form.errors)
    else:
        form = CahierDeCoursForm()

    # Passer la classe associée à l'enseignant au template
    return render(request, 'remplir_cahier.html', {'form': form, 'teacher': teacher, 'classes': classes})

def liste_cahiers(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    date_filter = request.GET.get('date', '')
    competence_filter = request.GET.get('competence', '')
    cahiers = CahierDeCours.objects.filter(teacher=teacher)
    
    if date_filter:
        cahiers = cahiers.filter(date=date_filter)
    
    if competence_filter:
        cahiers = cahiers.filter(competence__icontains=competence_filter)
    
    context = {
        'cahiers': cahiers,
        'teacher': teacher
    }
    return render(request, 'liste_cahier.html', context)

def create_planning(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            planning = form.save(commit=False)
            Planning.objects.create(
                    date=planning.date,
                    premiere_heure=planning.premiere_heure,
                    deuxieme_heure=planning.deuxieme_heure,
                    troisieme_heure=planning.troisieme_heure,
                    activite1=planning.activite1,
                    activite2=planning.activite2,
                    activite3=planning.activite3,
                    salle=planning.salle,
                    professeur=planning.professeur
                )
            return redirect('planning_list') 
    else:
        form = PlanningForm()
    return render(request, 'create_planning.html', {'form': form})

def planning_list(request):
    planning = Planning.objects.all()
    return render(request, 'planning_list.html', {'planning': planning})

def planning_student(request):
    planning = Planning.objects.all()
    return render(request, 'planning_etudiant.html', {'planning': planning})

@login_required
def send_planning(request):
    if request.method == 'POST':
        selected_plannings = request.POST.getlist('plannings')
        
        if not selected_plannings:
            messages.error(request, 'Aucun planning sélectionné.')
            return redirect('list_plannings')
        
        plannings = Planning.objects.filter(id__in=selected_plannings)

        if 'envoyer' in request.POST:
            return redirect('select_recipients', planning_ids=','.join(selected_plannings))
        
    return redirect('list_plannings')


def env_planning(request):
    plannings = Planning.objects.all()
    return render(request, 'list_plannings.html', {'plannings': plannings})

def edit_planning(request, pk):
    planning = get_object_or_404(Planning, pk=pk)
    if request.method == 'POST':
        form = PlanningForm(request.POST, instance=planning)
        if form.is_valid():
            form.save()
            return redirect('planning_list')
    else:
        form = PlanningForm(instance=planning)
    return render(request, 'edit_planning.html', {'form': form})

def delete_planning(request, pk):
    planning = get_object_or_404(Planning, pk=pk)
    if request.method == 'POST':
        planning.delete()
        return redirect('planning_list')
    return render(request, 'supprimer_planning.html', {'planning': planning})

def planning_list(request):
    plannings = Planning.objects.all()
    return render(request, 'planning_list.html', {'plannings': plannings})

def filter_planning(request):
    plannings = Planning.objects.all()
    
    id = request.GET.get('id')
    date = request.GET.get('date')
    
    if id:
        plannings = plannings.filter(id=id)
    elif date:
        plannings = plannings.filter(date__icontains=date)
    return render(request, 'filter_planning.html' , {'plannings':plannings})