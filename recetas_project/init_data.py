import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recetas_project.settings')
django.setup()

from recetas_app.models import Categoria

# Crear categorías
categorias_data = [
    ('Comida Rápida', '🍕', 'Recetas rápidas y deliciosas para cuando tienes prisa'),
    ('Postres 15min', '🍰', 'Postres que puedes preparar en 15 minutos'),
    ('Ensaladas', '🥗', 'Ensaladas frescas y saludables'),
    ('Tacos', '🌮', 'Variedad de tacos para todos los gustos'),
    ('Pastas', '🍝', 'Deliciosas recetas de pasta'),
    ('Sopas', '🍲', 'Sopas reconfortantes y nutritivas'),
]

for nombre, icono, descripcion in categorias_data:
    categoria, created = Categoria.objects.get_or_create(
        nombre=nombre,
        defaults={'icono': icono, 'descripcion': descripcion}
    )
    if created:
        print(f"✓ Categoría '{nombre}' creada")
    else:
        print(f"✓ Categoría '{nombre}' ya existe")

print("\n✅ Base de datos inicializada correctamente")
