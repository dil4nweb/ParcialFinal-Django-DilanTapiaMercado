# Parcial Final - Django y PythonAnywhere

**Estudiante:** Dilan Tapia Mercado

Proyecto de ejemplo completo compatible con la estructura `my_project`/`myapp` del repositorio del curso. **No es un clon literal del repositorio del profesor**: si la evaluación exige conservar todo el código previo, integrar estos cambios sobre el clon original.

## Windows CMD

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
set DJANGO_DEBUG=True
python manage.py runserver
```

Abrir http://127.0.0.1:8000/programas/crear/ y http://127.0.0.1:8000/admin/.

La base de datos `db.sqlite3` incluye cinco programas de ejemplo. Las migraciones del modelo Programa ya están marcadas como aplicadas; `migrate` completará las tablas de administración y autenticación. **No hay superusuario precargado.**

## GitHub

Crear repositorio público vacío `ParcialFinal-Django-DilanTapiaMercado`. Dentro de esta carpeta:

```cmd
git init
git branch -M main
git remote add origin https://github.com/dil4nweb/ParcialFinal-Django-DilanTapiaMercado.git
git add .
git commit -m "Parcial final Django con programas y SQLite"
git push -u origin main
```

No subir contraseñas, archivos `.env` ni el entorno `venv`.

## PythonAnywhere (consola Bash)

```bash
git clone https://github.com/dil4nweb/ParcialFinal-Django-DilanTapiaMercado.git
python3 -m venv venv
source venv/bin/activate
cd ParcialFinal-Django-DilanTapiaMercado
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

En Web, elegir **Manual configuration**, la versión Python compatible y Virtualenv `/home/TU_USUARIO/venv`. WSGI:

```python
import os
import sys
path = '/home/TU_USUARIO/ParcialFinal-Django-DilanTapiaMercado'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Static files: URL `/static/`, directory `/home/TU_USUARIO/ParcialFinal-Django-DilanTapiaMercado/static_publico`. Pulsar **Reload**. Verificar `/programas/crear/` y `/admin/`. Cambiar la SECRET_KEY por una variable de entorno privada antes de publicar.
