from django.contrib import admin
from auth_app.models import Student, Teacher, Note, Classe,Salle, Matiere, Filiere, Comptable, Administrateur, ResponsableFiliere, ResponsableClasse

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Administrateur)
admin.site.register(ResponsableFiliere)
admin.site.register(ResponsableClasse)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Salle)
admin.site.register(Comptable)
admin.site.register(Filiere)
admin.site.register(Note)
