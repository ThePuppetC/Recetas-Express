#!/bin/bash

echo "🍳 Recetas Express - Iniciando servidor..."
echo ""

cd /workspaces/Recetas-Express/recetas_project
python manage.py runserver 0.0.0.0:8000
