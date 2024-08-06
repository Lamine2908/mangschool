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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.inscription, name='inscription'),
    path('', views.connexion, name='connexion'),
    
    path('acceuil/', views.index, name='index'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('notification/', views.notification, name='notification'),
]
