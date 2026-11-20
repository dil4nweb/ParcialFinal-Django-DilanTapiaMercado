from django import forms
from .models import Programa
class ProgramaForm(forms.ModelForm):
 class Meta:
  model=Programa
  fields=['codigo','nombre','estado','facultad']
  widgets={'codigo':forms.TextInput(attrs={'placeholder':'Ej: ING001'}),'nombre':forms.TextInput(attrs={'placeholder':'Nombre del programa'}),'facultad':forms.TextInput(attrs={'placeholder':'Facultad'})}
