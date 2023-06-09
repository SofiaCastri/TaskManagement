from django import forms
from .models import Task
from django.contrib.auth.models import User
from .models import Gruppo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nome', 'descrizione', 'data_inizio', 'data_fine', 'categoria', 'gestione']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            self.add_error('nome', 'Il campo nome è obbligatorio.')
        return nome

    def clean_task(self):
        task = self.cleaned_data.get('task')
        if not task:
            self.add_error('task', 'Il campo task è obbligatorio.')
        return task

    def clean(self):
        cleaned_data = super().clean()
        data_inizio = cleaned_data.get('data_inizio')
        data_fine = cleaned_data.get('data_fine')
        if data_inizio and data_fine and data_inizio > data_fine:
            self.add_error('data_fine', 'La data di fine deve essere successiva alla data di inizio.')

class ModificaTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['stato', 'categoria', 'gestione']




###########################
class GruppoForm(forms.ModelForm):
        utenti = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

        class Meta:
                model = Gruppo
                fields = ['nome', 'descrizione', 'data_inizio', 'data_fine', 'categoria', 'gestione', 'utenti']

class ModificaGruppoForm(forms.ModelForm):
    utenti = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Task
        fields = ['stato', 'categoria', 'gestione', 'utenti']

