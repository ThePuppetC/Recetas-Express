# Recetas Express 🍳

Una aplicación web Django moderna para compartir, descubrir y puntuar recetas.

## 🚀 Características

- ✅ Compartir recetas con imágenes, ingredientes e instrucciones detalladas
- ✅ Sistema de puntuación (1-5 estrellas) con comentarios
- ✅ Perfiles de usuario personalizables con foto de perfil
- ✅ Búsqueda y filtrado de recetas por categoría, dificultad y tiempo
- ✅ Sistema de autenticación completo (registro, login, logout)
- ✅ Base de datos SQLite integrada
- ✅ Interfaz responsiva con Bootstrap 5
- ✅ Diseño moderno y atractivo similar a "Recetas Express"

## 📋 Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)
- SQLite (incluido en Python)

## 🔧 Instalación Rápida

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar migraciones de base de datos
```bash
cd recetas_project
python manage.py migrate
```

### 3. Crear superusuario (administrador)
```bash
python manage.py createsuperuser
```

### 4. Inicializar categorías
```bash
python ../init_data.py
```

## ▶️ Ejecutar la aplicación

```bash
cd recetas_project
python manage.py runserver
```

La aplicación estará disponible en: **http://127.0.0.1:8000/**

## 🔐 Acceder al Panel de Administración

1. Ir a: `http://127.0.0.1:8000/admin/`
2. Ingresar con tus credenciales de superusuario

## 📁 Estructura del Proyecto

```
Recetas-Express/
├── recetas_project/          # Proyecto Django
│   ├── recetas_project/      # Configuración
│   │   ├── settings.py       # Configuración Django
│   │   ├── urls.py           # Rutas principales
│   │   └── wsgi.py           # WSGI para despliegue
│   ├── recetas_app/          # Aplicación principal
│   │   ├── models.py         # Modelos de datos
│   │   ├── views.py          # Vistas
│   │   ├── forms.py          # Formularios
│   │   ├── urls.py           # Rutas
│   │   ├── templates/        # Plantillas HTML
│   │   ├── static/           # CSS, JS
│   │   └── migrations/       # Migraciones
│   ├── manage.py             # Gestión Django
│   └── db.sqlite3            # Base de datos
├── requirements.txt          # Dependencias
├── init_data.py              # Script de inicialización
├── README.md                 # Este archivo
└── LICENSE                   # Licencia MIT
```

## 📦 Modelos de Datos

### 🏷️ Categoria
- Nombres únicos de categorías
- Icono y descripción
- Recuento automático de recetas

### 🍳 Receta
- Título, descripción, ingredientes, instrucciones
- Tiempo de preparación y cocción
- Nivel de dificultad (Fácil, Medio, Difícil)
- Imagen asociada
- Autor (usuario que la compartió)
- Timestamps de creación y actualización

### ⭐ Puntuacion
- Sistema de 1-5 estrellas
- Comentarios opcionales
- Una puntuación por usuario por receta
- Timestamps de creación y actualización

### 👤 PerfilUsuario
- Biografía y foto de perfil
- Ciudad y país
- Preferencias dietéticas
- Estadísticas automáticas

## 🎨 Personalización

### Cambiar colores principales
Edita `/recetas_app/static/css/style.css`:
```css
:root {
    --color-primary: #2ecc71;  /* Verde */
    --color-light: #f8f9fa;
    --color-dark: #2c3e50;
}
```

### Agregar nuevas categorías
1. Ve al panel de administración: `/admin/`
2. O edita `/recetas_project/init_data.py` y ejecuta `python ../init_data.py`

## 📱 URLs Principales

- `/` - Página de inicio
- `/recetas/` - Listar todas las recetas
- `/recetas/crear/` - Crear nueva receta
- `/recetas/<id>/` - Detalle de receta
- `/recetas/<id>/puntuar/` - Puntuar receta
- `/mis-recetas/` - Mis recetas (requiere login)
- `/perfil/<username>/` - Perfil público del usuario
- `/editar-perfil/` - Editar mi perfil
- `/categorias/` - Ver categorías
- `/registro/` - Registrarse
- `/login/` - Iniciar sesión
- `/logout/` - Cerrar sesión
- `/admin/` - Panel administrativo

## 🚀 Despliegue

### Heroku
```bash
# 1. Crear Procfile
echo "web: gunicorn recetas_project.wsgi" > Procfile

# 2. Crear runtime.txt
echo "python-3.10.5" > runtime.txt

# 3. Instalar gunicorn
pip install gunicorn

# 4. Desplegar
heroku create tu-app
git push heroku main
```

### PythonAnywhere
1. Subir el código a GitHub
2. Crear una app web en PythonAnywhere
3. Configurar la aplicación Django
4. Usar SQLite o PostgreSQL

### AWS/DigitalOcean
- Usar nginx como servidor web
- Gunicorn como servidor de aplicación
- PostgreSQL para producción
- CloudFront para servir estáticos

## 🐛 Solución de Problemas

### Error: "No module named 'django'"
```bash
pip install -r requirements.txt
```

### Error: "table doesn't exist"
```bash
python manage.py migrate
```

### Error de permiso en archivos estáticos
```bash
python manage.py collectstatic --noinput
chmod -R 755 recetas_app/static/
```

### Las imágenes no se cargan
- Asegúrate de que la carpeta `media/` existe
- Verifica la ruta en `settings.py`
- En producción, usa un servicio CDN

## 📝 Licencia

MIT License - Ver LICENSE para más detalles

## 💡 Tips

- Crea un usuario de prueba para probar todas las funcionalidades
- Agrega imágenes de recetas para mejor visualización
- Personaliza el CSS según tus preferencias
- Usa el panel de administración para gestionar contenido

---

**¡Diviértete compartiendo tus mejores recetas! 🍳👨‍🍳**

Desarrollado con ❤️ usando Django y Bootstrap 5