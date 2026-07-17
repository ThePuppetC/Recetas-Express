#!/bin/bash
set -e

echo "🍳 Recetas Express - Crear Superusuario"
echo "========================================"
echo ""

cd /workspaces/Recetas-Express/recetas_project

USERNAME="${DJANGO_SUPERUSER_USERNAME:-${1:-admin}}"
EMAIL="${DJANGO_SUPERUSER_EMAIL:-${2:-admin@example.com}}"
PASSWORD="${DJANGO_SUPERUSER_PASSWORD:-${3:-admin123}}"

export DJANGO_SUPERUSER_USERNAME="$USERNAME"
export DJANGO_SUPERUSER_EMAIL="$EMAIL"
export DJANGO_SUPERUSER_PASSWORD="$PASSWORD"

python manage.py migrate --noinput

python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

user, created = User.objects.get_or_create(username=username, defaults={'email': email})
user.email = email
user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()

print(f'Superusuario listo: {username}')
"
