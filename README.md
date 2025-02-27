# Pautas principales
Cuenta en git
Crear repositorio
Crear ssh
Vincular repositorio en oredenador local
Crear entorno virtual
Verificar instalacion python y version 



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