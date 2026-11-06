#Requisitos previos
 -Python 3.13.2 o superior
 -un gestor de paquetes de python (como pip)

#instalacion y configuracion
   ```bash
   git clone https://github.com/Richard-OnO/CER2-MendozaRicardo.git
   cd TallerDjango

#Crear y activar el entorno virtual
 python -m venv venv
 venv\Scripts\activate

#instalar dependencias
 pip install -r requirements.txt

#Aplicar migraciones de la base de datos
 python manage.py migrate

#crear el superusuario
 python manage.py createsuperuser

#iniciar el servidor 
 python manage.py runserver