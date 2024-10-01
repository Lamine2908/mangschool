"""
URL configuration for fize_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from django.contrib import admin
from django.urls import path
from auth_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.inscription, name='inscription'),
    path('', views.connexion, name='connexion'),
    path("navigation/", views.navigation, name="navigation"),
    path('acceuil/', views.index, name='index'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('student/', views.student_list, name='student_list'),
    path('detail_eleve/<int:student_id>/', views.student_detail, name='student_detail'),
    path('detail_prof/<int:teacher_id>/', views.detail_prof, name='detail_prof'),
    path('filter_students_view/', views.filter_students_view, name='filter_students_view'),
    path('filter_teacher/', views.filter_teacher, name='filter_teacher'),
    path('teacher/', views.teacher_list, name='teacher_list'),
    path('student_add/', views.add_student, name='add_student'),
    path('teacher_add/', views.add_teacher, name='add_teacher'),
    path('espaceadmins', views.espaceadmins, name='espaceadmins'),
    path('teacher/update/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('student/update/<int:student_id>/', views.update_student, name='update_student'),
    path('suprof/<int:id>/', views.delete_teacher_by_id, name='delete_teacher_by_id'),
    path('supeleve/<int:student_id>/', views.delete_student_by_id, name='delete_student_by_id'),
    path('comptable/', views.comptable, name='comptable'),
    # path('comptable_view/', views.comptable_view, name='comptable_view'),
    path('create_planning/', views.create_planning, name='create_planning'),
    # path('planning_etudiant/', views.planning_student, name='planning_student'),
    path('parametre_filiere/<int:responsable_id>/', views.parametre_filiere, name='parametre_filiere'),    
    path('espaceeleve/<int:student_id>/', views.espaceeleve, name='espaceeleve'),
    path('espaceeleves/', views.espaceseleves, name='espaceseleves'),
    path('espaceprof/<int:teacher_id>/', views.espaceprof, name='espaceprof'),
    path('espaceadmin/<int:admin_id>/', views.espaceadmin, name='espaceadmin'),
    path('responsableclasse/<int:responsable_id>', views.responsableclasse, name='responsableclasse'),
    path('responsableclasse/', views.espaceresponsableclasse, name='espaceresponsableclasse'),
    path('responsables_filieres/', views.responsables_filieres, name='responsables_filieres'),
    path('responsable_filiere/<int:responsable_id>', views.responsable_filiere, name='responsable_filiere'),
    # path('paiement/<int:student_id>/', views.paiement_etudiant, name='paiement_etudiant'),
    # path('paiement_liste/', views.paiement_liste, name='paiement_liste'),
    # path('valider-paiement/<int:paiement_id>/', views.valider_paiement, name='valider_paiement'),
    # path('liste-paiements/', views.paiement_liste, name='paiement_liste'),
    path('ajouter_classe/', views.ajouter_classe, name='ajouter_classe'),
    path('liste_classes/', views.liste_classes, name='liste_classes'),
    path('teacher/<int:teacher_id>/', views.prof_etudiant_list, name='prof_etudiant_list'),
    path('ajouter_note/<int:teacher_id>/', views.ajouter_notes, name='ajouter_notes'),
    path('afficher_notes/<int:teacher_id>/', views.afficher_notes, name='afficher_notes'),
    path('modifier_notes/<int:note_id>/', views.modifier_notes, name='modifier_notes'),
    path('ajouter_salle/', views.ajouter_salle, name='ajouter_salle'),
    path('liste_salle/', views.liste_salles, name='liste_salles'),
    path('classes/ajouter/', views.ajouter_classe, name='ajouter_classe'),
    path('classes/modifier/<int:id>/', views.modifier_classe, name='modifier_classe'),
    path('classes/supprimer/<int:id>/', views.supprimer_classe, name='supprimer_classe'),
    path('salles/', views.liste_salles, name='liste_salles'),
    path('salles/ajouter/', views.ajouter_salle, name='ajouter_salle'),
    path('salles/modifier/<int:id>/', views.modifier_salle, name='modifier_salle'),
    path('salles/supprimer/<int:id>/', views.supprimer_salle, name='supprimer_salle'),
    path('planning/', views.planning_list, name='planning_list'),
    path('planning/delete/<int:pk>/', views.delete_planning, name='delete_planning'),
    path('planning/edit/<int:pk>/', views.edit_planning, name='edit_planning'),
    # path('comptable/', views.comptable_list, name='comptable_list'),
    path('comptable/<int:id>/', views.espacecomptable, name='espacecomptable'),
    # path('comptable_detail/<int:id>/', views.comptable_detail, name='comptable_detail'),
    # path('comptable/<int:id>/edit/', views.comptable_edit, name='comptable_edit'),
    # path('comptable/<int:id>/delete/', views.comptable_delete, name='comptable_delete'),
    # path('paiements/', views.view_teacher_payments, name='view_teacher_payments'),
    # path('manage_payments/', views.manage_payments, name='manage_payments'),
    # path('payment_list/', views.payment_list, name='payment_list'),
    path('affecter_prof/<int:teacher_id>/', views.assign_teacher_to_classes, name='assign_teacher_to_classes'),
    path('teacher_class/', views.teacher_class, name='teacher_class'),   
    path('affecter_eleve/<int:student_id>/', views.Affecter_eleve, name='Affecter_eleve'),
    path('liste_classe/', views.liste_classe, name='liste_classe'),
    path('class_info/', views.class_info, name='class_info'),
    path('remplir-cahier/<int:teacher_id>/', views.remplir_cahier, name='remplir_cahier'),
    path('liste_cahiers/<int:teacher_id>/',views.liste_cahiers, name='liste_cahiers'),
    path('send_planning/', views.send_planning, name='send_planning'),
    path('env_planning/', views.env_planning, name='env_planning'),
    path('filter_planning/', views.filter_planning, name='filter_planning'),
    path('ajouter_matiere/', views.ajouter_matiere, name='ajouter_matiere'),
    path('modifier_matiere/<int:matiere_id>/', views.modifier_matiere, name='modifier_matiere'),
    path('supprimer_matiere/<int:matiere_id>/', views.supprimer_matiere, name='supprimer_matiere'),
    path('liste_matieres/', views.liste_matieres, name='liste_matieres'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
