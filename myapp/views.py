from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProgramaForm
from .models import Programa
def crear_programa(request):
 form=ProgramaForm(request.POST or None)
 if request.method=='POST' and form.is_valid():
  form.save()
  messages.success(request,'Programa registrado correctamente.')
  return redirect('crear_programa')
 return render(request,'myapp/crear_programa.html',{'form':form,'total':Programa.objects.count()})
