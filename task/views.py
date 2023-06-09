from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth import login
from django.contrib.contenttypes.models import ContentType
from .models import Task
from task.models import Task
from .models import Categoria
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout
from .form import TaskForm
from .form import ModificaTaskForm
from .form import ModificaGruppoForm
from django.shortcuts import render, redirect
from .form import GruppoForm
from .models import Gruppo



# Create your views here.
#la vista è una funzione che riceverà la richiesta dell'utente che ritornerà una pagina html

def taskHome(request):
    return render(request, 'Home.html') #la funzione render già importanta prende in ingresso la request e una stringa che indica la pagina web da visualizzare

def Iscrizione(request):
    return render(request, 'Iscriviti.html')

def Login(request):
    return render(request, 'Login.html')

def RegistrazioneCompletata(request):
    return render(request, 'RegistrazioneCompletata.html')

def Accesso(request):
    now = timezone.now()
    tasks = Task.objects.all()
    gruppos=Gruppo.objects.all()
    tasks_utente = Task.objects.filter(utente=request.user)
    tasks_pubblici = Task.objects.filter(gestione='pubblico').exclude(utente=request.user)
    gruppo_pubblici = Gruppo.objects.filter(gestione='pubblico')
    context = {
        'now': now,
        'tasks': tasks,
        'gruppos': gruppos,
        'categorie': Categoria.objects.all(),
        'tasks_utente': tasks_utente,
        'tasks_pubblici': tasks_pubblici,
        'gruppo_pubblici': gruppo_pubblici,
        'users': User.objects.all(),
    }

    return render(request, 'Accesso.html', context)

def dettaglio_gruppo(request, gruppo_id):
    gruppo = Gruppo.objects.get(id=gruppo_id)
    context = {
        'gruppo': gruppo
    }
    return render(request, 'Accesso.html', context)






def register(request):
    if request.method == 'POST' and request.POST.get('Password') == request.POST.get('PasswordC'):
        username = request.POST.get('Username')
        firstname = request.POST.get('FirstName')
        lastname = request.POST.get('LastName')
        password = request.POST.get('Password')
        email = request.POST.get('Email')

        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password,
                                        email=email)

        content_type = ContentType.objects.get_for_model(Task)  # Sostituisci Task con il modello desiderato
        permission = Permission.objects.get(content_type=content_type,
                                            codename='add_task')  # Sostituisci 'add_task' con il codename del permesso desiderato
        user.user_permissions.add(permission)

        return redirect('RegistrazioneCompletata')
    else:
        return render(request, 'Iscriviti.html')


###################################################

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.utente = request.user
            categoria_nome = form.cleaned_data['categoria']
            gestione = form.cleaned_data['gestione']
            try:
                categoria = Categoria.objects.get(nome=categoria_nome)
                task.categoria = categoria
                task.gestione = gestione
                task.save()
                return redirect('Accesso')
            except Categoria.DoesNotExist:
                form.add_error('categoria', 'Seleziona una categoria valida')
        else:
            print(form.errors)
    else:
        form = TaskForm()

    context = {
        'form': form,
        'categorie': Categoria.CATEGORIE,
    }

    return render(request, 'CreaTask.html', context)







##############################################################################################
def modifica_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = ModificaTaskForm(instance=task)

    if request.method == 'POST':
        # Gestisci il salvataggio delle modifiche al Task
        task.nome = request.POST['nome']
        task.descrizione = request.POST['descrizione']
        task.data_inizio = request.POST['data_inizio']
        task.data_fine = request.POST['data_fine']
        task.stato = request.POST['stato']
        task.categoria_id = request.POST['categoria']
        task.gestione = request.POST['gestione']
        task.save()

        # Reindirizza all'URL dei dettagli del Task dopo aver salvato le modifiche
        return redirect('Accesso')

    return render(request, 'ModificaTask.html', {'task': task, 'form': form})


########################################################################
#eliminazione del task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('Accesso')

def delete_gruppo(request, gruppo_id):
    gruppo = get_object_or_404(Gruppo, id=gruppo_id)
    gruppo.delete()
    return redirect('Accesso')


def registerLogin(request):
    user = request.POST.get('Username')
    email = request.POST.get('Email')
    password = request.POST.get('Password')
    user=authenticate(username=user, email=email, password=password)
    if user is not None:
        login(request,user)
        return redirect('Accesso')
    else:
        return redirect('Home')



def logout_view(request):
    logout(request)
    # Redirect to a success page.


################creiamo una vista per la creazione di un task di gruppo

###################################################################à


def create_gruppo(request):
    if request.method == 'POST':
        form = GruppoForm(request.POST)
        if form.is_valid():
            categoria_nome = form.cleaned_data['categoria']
            gestione = form.cleaned_data['gestione']
            utenti = request.POST.getlist('utenti')
            try:
                categoria = Categoria.objects.get(nome=categoria_nome)
                gruppo = Gruppo.objects.create(
                    nome=form.cleaned_data['nome'],
                    descrizione=form.cleaned_data['descrizione'],
                    data_inizio=form.cleaned_data['data_inizio'],
                    data_fine=form.cleaned_data['data_fine'],
                    categoria=categoria,
                    gestione=gestione
                )
                gruppo.utenti.set(utenti)  # Aggiungi gli utenti al gruppo
                return redirect('Accesso')
            except Categoria.DoesNotExist:
                form.add_error('categoria', 'Seleziona una categoria valida')
        else:
            print(form.errors)
    else:
        form = GruppoForm()

    context = {
        'form': form,
        'categorie': Categoria.CATEGORIE,
        'utenti': User.objects.all()
    }

    return render(request, 'CreaTaskTeam.html', context)


def modifica_gruppo(request, gruppo_id):
    gruppo = get_object_or_404(Gruppo, pk=gruppo_id)
    form = ModificaGruppoForm(instance=gruppo)

    if request.method == 'POST':
        # Gestisci il salvataggio delle modifiche al Task
        gruppo.nome = request.POST['nome']
        gruppo.descrizione = request.POST['descrizione']
        gruppo.data_inizio = request.POST['data_inizio']
        gruppo.data_fine = request.POST['data_fine']
        gruppo.stato = request.POST['stato']
        gruppo.categoria_id = request.POST['categoria']
        gruppo.gestione = request.POST['gestione']
        gruppo.utenti.set(request.POST.getlist('utenti'))
        gruppo.save()

        # Reindirizza all'URL dei dettagli del Task dopo aver salvato le modifiche
        return redirect('Accesso')
    context = {
        'gruppo': gruppo,
        'form': form,
        'utenti': User.objects.all()
    }

    return render(request, 'ModificaGruppo.html', context)

