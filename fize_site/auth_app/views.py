from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm

from auth_app.models import Student, Teacher
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else :
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form' : form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else :
            messages.error(request, 'Informations de connexion incorrectes.')
    return render(request, 'connexion.html')

def index(request):
    return render(request, 'index.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})
def student_add(request):
    return render(request, 'student_add.html')
def notification(request):
    return render(request, 'notification.html')