# 🍳 Recetas Express - Guía de Uso

## ¿Qué se ha creado?

Se ha desarrollado una aplicación **Django completa** para compartir recetas con todas las funcionalidades que solicitaste:

### ✅ Funcionalidades Implementadas

1. **Compartir Recetas**
   - Crear, editar y eliminar recetas
   - Carga de imágenes
   - Ingredientes e instrucciones
   - Tiempo de preparación, cocción, porciones
   - Niveles de dificultad

2. **Ver Recetas**
   - Página de inicio con recetas populares
   - Listado completo con filtros
   - Búsqueda por nombre, categoría, dificultad
   - Ordenamiento por tiempo

3. **Puntuar Recetas**
   - Sistema de 1-5 estrellas
   - Comentarios por receta
   - Promedio de calificaciones
   - Una puntuación por usuario por receta

4. **Perfiles de Usuario**
   - Información personal (nombre, ciudad, país)
   - Foto de perfil
   - Biografía
   - Preferencias dietéticas
   - Estadísticas (recetas compartidas, puntuaciones recibidas)

5. **Base de Datos SQLite**
   - Totalmente funcional
   - Modelos: Categoria, Receta, Puntuacion, PerfilUsuario
   - Índices optimizados para búsquedas

6. **Autenticación**
   - Registro de nuevos usuarios
   - Login seguro
   - Logout
   - Panel de administración Django

## 📱 Estructura de la Aplicación

```
Recetas-Express/
├── recetas_project/
│   ├── manage.py                    # Gestor de Django
│   ├── db.sqlite3                   # Base de datos
│   ├── init_data.py                 # Script de categorías
│   ├── recetas_project/
│   │   ├── settings.py              # Configuración
│   │   ├── urls.py                  # Rutas
│   │   └── wsgi.py                  # WSGI
│   └── recetas_app/
│       ├── models.py                # Modelos
│       ├── views.py                 # Vistas
│       ├── forms.py                 # Formularios
│       ├── urls.py                  # URLs
│       ├── admin.py                 # Panel admin
│       ├── signals.py               # Señales
│       ├── static/css/style.css     # Estilos
│       └── templates/               # Templates HTML
├── requirements.txt                 # Dependencias
└── run.sh                          # Script para iniciar
```

## 🚀 Guía Rápida

### 1. Instalar dependencias (ya se hizo)
```bash
pip install -r requirements.txt
```

### 2. Crear superusuario (administrador)
```bash
./create_admin.sh
```

O manualmente:
```bash
cd recetas_project
python manage.py createsuperuser
```

### 3. Iniciar servidor
```bash
./run.sh
```

O manualmente:
```bash
cd recetas_project
python manage.py runserver
```

### 4. Acceder a la aplicación

**Aplicación principal:** http://127.0.0.1:8000/

**Panel de administración:** http://127.0.0.1:8000/admin/

## 📖 Rutas de la Aplicación

- `/` - Página de inicio
- `/recetas/` - Listar todas las recetas
- `/recetas/crear/` - Crear nueva receta
- `/recetas/<id>/` - Ver detalles de receta
- `/recetas/<id>/editar/` - Editar receta
- `/recetas/<id>/eliminar/` - Eliminar receta
- `/recetas/<id>/puntuar/` - Puntuar receta
- `/mis-recetas/` - Mis recetas (requiere login)
- `/perfil/<username>/` - Ver perfil usuario
- `/editar-perfil/` - Editar mi perfil
- `/categorias/` - Ver categorías
- `/categorias/<nombre>/` - Recetas de categoría
- `/registro/` - Registrarse
- `/login/` - Iniciar sesión
- `/logout/` - Cerrar sesión
- `/admin/` - Panel de administración

## 🎨 Diseño y Estilos

- **Framework CSS:** Bootstrap 5
- **Colores:** Verde principal (#2ecc71) - personalizable
- **Responsive:** Compatible con móvil, tablet y escritorio
- **Animaciones:** Transiciones suaves en tarjetas y botones

## 🔐 Panel de Administración

En `/admin/` puedes:
- Crear/editar categorías
- Ver todas las recetas
- Administrar usuarios
- Ver puntuaciones y comentarios
- Configurar preferencias

## 📂 Carpetas Importantes

- `media/` - Imágenes de recetas y perfiles (se crea automáticamente)
- `staticfiles/` - Archivos estáticos (para producción)
- `recetas_app/templates/` - Templates HTML
- `recetas_app/static/css/` - Estilos CSS

## 🐛 Troubleshooting

**Error: "No such table"**
```bash
python manage.py migrate
```

**Error: "No module named Django"**
```bash
pip install -r requirements.txt
```

**Las imágenes no se ven**
- Asegúrate de subir imágenes en formato JPG o PNG
- Verifica que la carpeta `media/` existe

**Puertos en uso**
```bash
python manage.py runserver 8001
```

## 💡 Próximos Pasos

1. **Crear usuario administrador** con `./create_admin.sh`
2. **Iniciar servidor** con `./run.sh`
3. **Crear usuario normal** en `/registro/`
4. **Compartir tu primera receta** en `/recetas/crear/`
5. **Explorar funcionalidades** - crear, buscar, puntuar

## 🤖 Commit automático de cambios

Si quieres dejar guardados automáticamente los cambios nuevos del proyecto, puedes usar el script incluido:

```bash
chmod +x auto_commit.sh
./auto_commit.sh
```

También puedes pasar un mensaje personalizado:

```bash
./auto_commit.sh "Actualización de recetas y mejoras visuales"
```

Este script:
- agrega todos los cambios nuevos al staging area,
- crea un commit con el mensaje indicado,
- lo sube al remoto con `git push`.

> Recomendación: usa un mensaje claro y específico para cada lote de cambios.

## 📝 Notas

- La base de datos está en `recetas_project/db.sqlite3`
- Las imágenes se guardan en `recetas_project/media/`
- El sitio está completamente funcional y listo para usar
- Puedes personalizar colores, fuentes y diseño en `style.css`

## 🎯 Variables de Entorno (Opcional)

Para producción, crea un archivo `.env`:
```
DEBUG=False
SECRET_KEY=tu-clave-secreta
ALLOWED_HOSTS=tu-dominio.com
```

---

**¡Estoy listo para empezar! 🍳👨‍🍳**

Cualquier duda, revisa el README.md principal o el código en `recetas_app/`
