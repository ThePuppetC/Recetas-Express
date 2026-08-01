#!/bin/bash

echo "🍳 Recetas Express - Setup"
echo "=========================="
echo ""

# Ir al directorio del proyecto
cd recetas_project

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r ../requirements.txt

# Realizar migraciones
echo "🔄 Ejecutando migraciones..."
python manage.py migrate

# Inicializar datos
echo "📝 Inicializando datos..."
python ../init_data.py

echo ""
echo "✅ ¡Setup completado!"
echo ""
echo "Para iniciar el servidor, ejecuta:"
echo "  cd recetas_project"
echo "  python manage.py runserver"
echo ""
echo "Para crear un superusuario, ejecuta:"
echo "  python manage.py createsuperuser"
