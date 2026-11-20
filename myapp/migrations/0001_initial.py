from django.db import migrations,models
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[migrations.CreateModel(name='Programa',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('codigo',models.CharField(max_length=20,unique=True)),('nombre',models.CharField(max_length=150)),('estado',models.BooleanField(default=True)),('facultad',models.CharField(max_length=150))],options={'verbose_name':'Programa','verbose_name_plural':'Programas'})]
