"""
URL configuration for TaskManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from task import views


#in questo file sono inclusi tutti gli URL accessibili dal nostro sito web
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.taskHome, name='Home'),
    path('taskHome/Iscriviti/', views.Iscrizione),
    path('taskHome/Iscriviti/Accesso/', views.register, name='register'),
    path('taskHome/Iscriviti/RegistrazioneCompletata/', views.RegistrazioneCompletata, name='RegistrazioneCompletata'),
    path('taskHome/Iscriviti/Accesso/pagina/', views.Accesso, name='Accesso'),


    path('taskHome/Iscriviti/Accesso/pagina/CreaTask/', views.create_task, name='create_task'),
    path('taskHome/Iscriviti/Accesso/pagina/CreaTaskTeam/', views.create_gruppo, name='create_gruppo'),

    path('taskHome/Iscriviti/Accesso/pagina/ModificaTask/<int:task_id>/', views.modifica_task, name='modifica_task'),
    path('taskHome/Iscriviti/Accesso/pagina/ModificaGruppo/<int:gruppo_id>/', views.modifica_gruppo, name='modifica_gruppo'),
    path('taskHome/Iscriviti/Accesso/pagina/<int:gruppo_id>/', views.dettaglio_gruppo, name='dettaglio_gruppo'),


    path('taskHome/Iscriviti/Accesso/pagina/delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('taskHome/Iscriviti/Accesso/pagina/delete_gruppo/<int:gruppo_id>/', views.delete_gruppo, name='delete_gruppo'),
    path('taskHome/Login/', views.Login, name='Login'),

    path('taskHome/Login/Accesso/pagina/', views.registerLogin, name="registerLogin"),

    path('taskHome/', views.logout_view, name="logout_view"),

]

