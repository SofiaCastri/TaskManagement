from django.contrib import admin
from .models import Task
from .models import Categoria
from .models import Gruppo
# Register your models here.
#serve per far si che nella pagina del superutente siano disponibili le tabelle dei modelli che creo in model.py

admin.site.register(Task)
admin.site.register(Categoria)
admin.site.register(Gruppo)