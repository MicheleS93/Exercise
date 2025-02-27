# Pautas principales

1.Preparacion entorno:
    Cuenta en git
    Crear repositorio
    Crear ssh en lcoal y vincular a cuenta git
    
    Verificar instalacion python y version 
    Vincular repositorio en ordenador local
    Crear entorno virtual
    Test commit 

2.Preparacion codigo:
    Lectura enunciado
    Estructura de carpetas recomendada


########################################################################################################

# Descargar proyecto de git
git clone "https link" or "ssh"
Para la ssh hay que crearla antes en el equipo, despues anadirla a git 

# Generar ssh
Verificar si ya tienes una clave SSH
    ls -al ~/.ssh

Generar una clave SSH
    ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"

Agregar la clave SSH a GitHub
    cat ~/.ssh/id_ed25519.pub

https://github.com/settings/keys
Haz clic en "New SSH Key"
Pon un nombre como "MacBook" y pega la clave copiada en el campo.

Porbar conexion 
    ssh -T git@github.com

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate
python --version

# Subidas a Git
Verificar si hay cambios 
    git status

Añadir los cambios al área de preparación
    git add .
    * Si solo quieres agregar archivos específicos
        git add archivo1.py archivo2.txt

Realiza un commit para registrar los cambios
    git commit -m "Mensaje descriptivo de los cambios realizados"

Para subir los cambios a tu repositorio remoto en GitHub
    git push origin main
    Si estás trabajando en una rama diferente a main, reemplaza main con el nombre de la rama en la que estás trabajando

# Estrucutra carpetas recomendada

📦 mi_proyecto/
 ┣ 📂 src/                  # Código fuente del proyecto
 ┃ ┣ 📂 modulo1/            # Un módulo específico (puedes tener varios)
 ┃ ┃ ┣ 📜 __init__.py       # Indica que este directorio es un paquete de Python
 ┃ ┃ ┣ 📜 clase1.py         # Definición de clases dentro del módulo
 ┃ ┃ ┣ 📜 clase2.py         
 ┃ ┣ 📜 main.py             # Punto de entrada principal del programa
 ┣ 📂 tests/                # Pruebas unitarias (usando unittest o pytest)
 ┃ ┣ 📜 test_clase1.py      
 ┃ ┣ 📜 test_clase2.py      
 ┣ 📂 docs/                 # Documentación del proyecto
 ┣ 📜 requirements.txt       # Dependencias del proyecto (si usas pip)
 ┣ 📜 .gitignore             # Archivos y carpetas a ignorar en Git
 ┣ 📜 README.md              # Descripción del proyecto
 ┣ 📜 setup.py               # (Opcional) Para convertirlo en un paquete instalable
