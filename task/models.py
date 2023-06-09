from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#ogni volta che si crea una classe bisogna fare la migrazione usando i comandi
#1. python manage.py makemigrations
#2. python manage.py migrate


#-------------------------------------------------
#ogni volta che si crea un nuovo modello bisogna scriverlo nel file adimin.py

class Categoria(models.Model):
    CATEGORIE=[
        ('Personale', 'Personale'),
        ('Lavoro', 'Lavoro'),
    ]
    nome = models.CharField(max_length=100, choices=CATEGORIE)

    def __str__(self):
        return self.nome



class Task(models.Model):
    STATUS_CHOICES = [
        ('da_fare', 'Da fare'),
        ('in_corso', 'In corso'),
        ('fatto', 'Fatto'),
    ]
    GESTIONE_CHOICES = [
        ('privato', 'Privato'),
        ('pubblico', 'Pubblico'),
    ]

    nome=models.CharField(max_length=100)
    descrizione=models.TextField()
    data_inizio=models.DateTimeField()
    data_fine=models.DateTimeField()
    stato = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='da_fare',
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    utente = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    gestione = models.CharField(
        max_length=20,
        choices=GESTIONE_CHOICES,
        default='privato',
    )

    def __str__(self):
        return self.nome




class Gruppo(models.Model):
    STATUS_CHOICES = [
        ('da_fare', 'Da fare'),
        ('in_corso', 'In corso'),
        ('fatto', 'Fatto'),
    ]
    GESTIONE_CHOICES = [
        ('privato', 'Privato'),
        ('pubblico', 'Pubblico'),
    ]

    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    data_inizio = models.DateTimeField()
    data_fine = models.DateTimeField()
    stato = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='da_fare',
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    utenti = models.ManyToManyField(User)  # relazione Molti a molti
    gestione = models.CharField(
        max_length=20,
        choices=GESTIONE_CHOICES,
        default='privato',
    )

    def __str__(self):
        return self.nome




