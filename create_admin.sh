#!/bin/bash

echo "🍳 Recetas Express - Crear Superusuario"
echo "========================================"
echo ""

cd /workspaces/Recetas-Express/recetas_project
python manage.py createsuperuser
