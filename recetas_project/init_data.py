import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recetas_project.settings')
django.setup()

from recetas_app.models import Categoria, Receta, PerfilUsuario
from django.contrib.auth.models import User

# Categorías
cats_data = [
    ('Comida Rápida', '🍕'), ('Postres', '🍰'), ('Ensaladas', '🥗'),
    ('Tacos', '🌮'), ('Pastas', '🍝'), ('Sopas', '🍲'),
    ('Bebidas', '🥤'), ('Desayunos', '🥞'),
]
cats = {}
for n, i in cats_data:
    c, _ = Categoria.objects.get_or_create(nombre=n, defaults={'icono': i})
    cats[n] = c

# Admin
admin, _ = User.objects.get_or_create(
    username='admin',
    defaults={'is_staff': True, 'is_superuser': True, 'email': 'admin@recetas.local', 'first_name': 'Chef'}
)
if not admin.has_usable_password():
    admin.set_password('admin123')
    admin.save()
PerfilUsuario.objects.get_or_create(usuario=admin)

# 40 Recetas variadas: (título, desc, ingredientes, instrucciones, t_prep, t_cocción, porciones, dificultad, categoría)
recetas = [
    ('Pizza Casera', 'Crujiente', 'Harina, tomate, queso, jamón', 'Mezcla, extiende, hornea', 15, 5, 4, 'Fácil', 'Comida Rápida'),
    ('Hamburguesa', 'Jugosa', 'Carne, pan, lechuga, tomate', 'Asa, arma', 10, 10, 2, 'Fácil', 'Comida Rápida'),
    ('Quesadilla', 'Rápida', 'Tortillas, queso, pollo', 'Cocina', 5, 5, 2, 'Fácil', 'Comida Rápida'),
    ('Sándwich Club', 'Clásico', 'Pan, pavo, jamón, queso', 'Arma', 5, 0, 1, 'Fácil', 'Comida Rápida'),
    ('Hot Dog BBQ', 'Sabroso', 'Salchichas, pan, cebolla, BBQ', 'Asa', 5, 3, 4, 'Fácil', 'Comida Rápida'),
    
    ('Brownies', 'Chocolate', 'Chocolate, huevo, harina', 'Mezcla, hornea', 10, 5, 9, 'Fácil', 'Postres'),
    ('Tiramisú', 'Italiano', 'Café, mascarpone, galletas', 'Moja, alterna', 20, 120, 8, 'Medio', 'Postres'),
    ('Flan', 'Cremoso', 'Leche, huevo, azúcar', 'Cocina, hornea', 15, 45, 6, 'Medio', 'Postres'),
    ('Fresas Chocolate', 'Romántico', 'Fresas, chocolate', 'Derrite, mojas', 10, 0, 4, 'Fácil', 'Postres'),
    ('Cheesecake', 'Sin horno', 'Queso crema, galletas, frutas', 'Mezcla, refrigera', 20, 120, 8, 'Fácil', 'Postres'),
    ('Tarta Manzana', 'Clásica', 'Manzana, harina, mantequilla', 'Arma, hornea', 20, 45, 8, 'Medio', 'Postres'),
    ('Mousse', 'Aireado', 'Frutas, crema, azúcar', 'Licúa, monta', 15, 60, 6, 'Fácil', 'Postres'),
    ('Crema Catalana', 'Tradicional', 'Leche, huevo, canela', 'Cocina, quema azúcar', 20, 30, 6, 'Medio', 'Postres'),
    
    ('Ensalada César', 'Con pollo', 'Lechuga, pollo, queso', 'Monta', 10, 15, 2, 'Fácil', 'Ensaladas'),
    ('Ensalada Griega', 'Fresca', 'Tomate, pepino, queso feta', 'Pica, mezcla', 10, 0, 2, 'Fácil', 'Ensaladas'),
    ('Caprese', 'Italiana', 'Tomate, mozzarella, albahaca', 'Alterna', 5, 0, 2, 'Fácil', 'Ensaladas'),
    ('Quinoa Bowl', 'Proteína', 'Quinoa, verduras, limón', 'Cocina, mezcla', 10, 15, 3, 'Fácil', 'Ensaladas'),
    ('Coleslaw', 'Americana', 'Col, zanahoria, mayonesa', 'Pica, mezcla', 10, 0, 4, 'Fácil', 'Ensaladas'),
    
    ('Tacos al Pastor', 'Mexicanos', 'Cerdo, piña, cebolla', 'Asa, sirve', 20, 30, 6, 'Medio', 'Tacos'),
    ('Tacos Pescado', 'Ligeros', 'Pescado, col, limón', 'Fríe, arma', 15, 10, 4, 'Medio', 'Tacos'),
    ('Tacos Pollo', 'Clásicos', 'Pollo, cebolla, cilantro', 'Cocina, sirve', 15, 20, 4, 'Fácil', 'Tacos'),
    
    ('Carbonara', 'Romana', 'Pasta, huevo, panceta, queso', 'Cocina, mezcla', 10, 10, 3, 'Fácil', 'Pastas'),
    ('Alfredo', 'Cremosa', 'Pasta, crema, queso', 'Cocina, mezcla', 10, 10, 3, 'Fácil', 'Pastas'),
    ('Boloñesa', 'Clásica', 'Pasta, carne, tomate', 'Simmer, cocina', 15, 45, 4, 'Fácil', 'Pastas'),
    ('Arrabbiata', 'Picante', 'Penne, tomate, ají', 'Salsa rápida', 10, 15, 2, 'Fácil', 'Pastas'),
    ('Ravioles Queso', 'Caseros', 'Pasta, ricotta, espinaca', 'Forma, cocina', 30, 15, 6, 'Difícil', 'Pastas'),
    
    ('Sopa Tomate', 'Reconfortante', 'Tomate, cebolla, ajo', 'Cocina, licúa', 15, 25, 4, 'Fácil', 'Sopas'),
    ('Minestrone', 'Vegetales', 'Verduras, pasta, frijoles', 'Cocina 30min', 20, 30, 6, 'Fácil', 'Sopas'),
    ('Pollo Clásica', 'Sanadora', 'Pollo, zanahoria, apio', 'Cocina lento', 15, 40, 4, 'Fácil', 'Sopas'),
    ('Champiñones', 'Elegante', 'Champiñones, crema', 'Sofríe, licúa', 15, 20, 3, 'Fácil', 'Sopas'),
    
    ('Batido Plátano', 'Energía', 'Plátano, leche, miel', 'Licúa', 5, 0, 1, 'Fácil', 'Bebidas'),
    ('Limonada', 'Refrescante', 'Limones, agua, azúcar', 'Exprime, mezcla', 10, 0, 6, 'Fácil', 'Bebidas'),
    ('Café Helado', 'Verano', 'Café, leche, azúcar', 'Mezcla, sirve', 5, 0, 1, 'Fácil', 'Bebidas'),
    
    ('Omelette', 'Proteína', 'Huevos, queso, jamón', 'Bate, cocina', 5, 5, 1, 'Fácil', 'Desayunos'),
    ('Pancakes', 'Esponjosos', 'Harina, huevo, leche', 'Mezcla, fríe', 10, 10, 4, 'Fácil', 'Desayunos'),
    ('Avena Frutas', 'Saludable', 'Avena, leche, plátano', 'Cocina, mezcla', 5, 10, 1, 'Fácil', 'Desayunos'),
    ('Tostadas Francesas', 'Crujientes', 'Pan, huevo, leche', 'Moja, fríe', 10, 10, 2, 'Fácil', 'Desayunos'),
    ('Huevos Revueltos', 'Con hierbas', 'Huevos, queso, perejil', 'Revuelve', 5, 5, 1, 'Fácil', 'Desayunos'),
    
    ('Ceviche', 'Peruano', 'Pescado, limón, cilantro', 'Cura en limón', 15, 20, 4, 'Medio', 'Comida Rápida'),
    ('Milanesa', 'Crispy', 'Carne, pan rallado, huevo', 'Empaña, fríe', 15, 15, 3, 'Fácil', 'Comida Rápida'),
]

for t, d, i, inst, tp, tc, p, dif, cat_n in recetas:
    Receta.objects.get_or_create(
        titulo=t,
        defaults={'descripcion': d, 'ingredientes': i, 'instrucciones': inst,
                  'tiempo_preparacion': tp, 'tiempo_coccion': tc, 'porciones': p,
                  'dificultad': dif, 'categoria': cats[cat_n], 'autor': admin,
                  'imagen': 'recetas/images/default.png'}
    )

print(f"✅ {Receta.objects.count()} recetas en BD")
