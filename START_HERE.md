# 🍳 RECETAS EXPRESS - INICIO RÁPIDO

## ✨ ¡Tu aplicación Django está lista!

Se ha creado una **aplicación web completa** para compartir recetas con todas las funcionalidades solicitadas.

---

## 🚀 PASO 1: Crear Administrador

En la terminal, ejecuta:

```bash
cd /workspaces/Recetas-Express
chmod +x create_admin.sh
./create_admin.sh
```

O manualmente:
```bash
cd /workspaces/Recetas-Express/recetas_project
python manage.py createsuperuser
```

Te pedirá:
- **Usuario:** (ej: admin)
- **Email:** (ej: admin@recetas.com)
- **Contraseña:** (ej: 123456)

---

## ▶️ PASO 2: Iniciar el Servidor

En la terminal, ejecuta:

```bash
chmod +x /workspaces/Recetas-Express/run.sh
/workspaces/Recetas-Express/run.sh
```

O manualmente:
```bash
cd /workspaces/Recetas-Express/recetas_project
python manage.py runserver
```

Verás algo como:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
```

---

## 🌐 PASO 3: Acceder a la Aplicación

### Aplicación Principal
👉 **http://127.0.0.1:8000/**

### Panel de Administración
👉 **http://127.0.0.1:8000/admin/**

(Usa las credenciales que creaste en el Paso 1)

---

## 📝 PASO 4: Crear Tu Primera Receta

1. Ve a http://127.0.0.1:8000/
2. Haz clic en **"Registrate"** para crear un usuario normal
3. O si ya iniciaste sesión como admin, ve a **"Compartir Receta"**
4. Completa el formulario:
   - **Título:** (ej: "Tacos al Pastor")
   - **Categoría:** (ej: "Tacos")
   - **Dificultad:** Fácil, Medio o Difícil
   - **Descripción:** Describe tu receta
   - **Ingredientes:** Uno por línea
   - **Instrucciones:** Paso a paso
   - **Tiempos:** Preparación y cocción
   - **Imagen:** Selecciona una foto

5. Haz clic en **"Compartir Receta"** ✅

---

## ⭐ PASO 5: Puntuar Recetas

1. Ve a cualquier receta
2. Haz clic en **"Calificar esta receta"**
3. Selecciona las estrellas (1-5)
4. Agrega un comentario (opcional)
5. Envía 🌟

---

## 📱 FUNCIONALIDADES PRINCIPALES

### 🏠 Inicio
- Recetas populares
- Categorías destacadas
- Acceso rápido

### 🔍 Explorar
- Buscar recetas
- Filtrar por categoría, dificultad, tiempo
- Ver paginación

### ➕ Crear
- Compartir tus recetas
- Con imagen y detalles completos
- Editar o eliminar cuando quieras

### 👤 Perfil
- Personalizar tu perfil
- Foto de perfil
- Bio y ubicación
- Preferencias dietéticas

### ⭐ Puntuar
- Calificación 1-5 estrellas
- Dejar comentarios
- Ver promedio de puntuaciones

---

## 📂 ARCHIVOS IMPORTANTES

```
/workspaces/Recetas-Express/
├── recetas_project/
│   ├── db.sqlite3              ← Base de datos
│   ├── media/                  ← Imágenes (se crea automáticamente)
│   ├── recetas_app/
│   │   ├── models.py           ← Modelos (Receta, Puntuacion, etc)
│   │   ├── views.py            ← Lógica de la app
│   │   ├── forms.py            ← Formularios
│   │   ├── templates/          ← Páginas HTML (14)
│   │   └── static/css/         ← Estilos CSS
│   └── manage.py               ← Gestor Django
├── README.md                   ← Documentación técnica
├── GUIA_USO.md                 ← Guía completa
└── run.sh                      ← Script para iniciar
```

---

## 🎨 PERSONALIZACIÓN

### Cambiar Colores
Edita: `/workspaces/Recetas-Express/recetas_project/recetas_app/static/css/style.css`

```css
:root {
    --color-primary: #2ecc71;  /* Verde - cambiar aquí */
}
```

### Cambiar Nombre
Edita: `/workspaces/Recetas-Express/recetas_project/recetas_project/settings.py`

```python
SITE_NAME = "Tu Nombre"
```

---

## 🐛 PROBLEMAS COMUNES

### Puerto 8000 en uso
```bash
python manage.py runserver 8001
```

### Imágenes no se ven
1. Reinicia el servidor
2. Verifica que la carpeta `media/` existe

### Error de permisos
```bash
chmod -R 755 /workspaces/Recetas-Express/recetas_project/recetas_app/static/
```

---

## 📞 RUTAS PRINCIPALES

| URL | Descripción |
|-----|-------------|
| `/` | Página de inicio |
| `/recetas/` | Listar todas las recetas |
| `/recetas/crear/` | Crear nueva receta |
| `/recetas/<id>/` | Ver detalles |
| `/recetas/<id>/puntuar/` | Puntuar receta |
| `/mis-recetas/` | Mis recetas |
| `/perfil/<username>/` | Ver perfil |
| `/editar-perfil/` | Editar mi perfil |
| `/categorias/` | Ver categorías |
| `/registro/` | Registrarse |
| `/login/` | Iniciar sesión |
| `/admin/` | Panel admin |

---

## 💡 TIPS

✅ **Crea varias recetas** para probar búsqueda y filtros

✅ **Carga buenas imágenes** para mejor visualización

✅ **Puntúa recetas de otros usuarios** para ver el sistema de calificación

✅ **Personaliza tu perfil** con foto y bio

✅ **Explora el panel admin** en `/admin/`

---

## 🎯 CHECKLIST DE INSTALACIÓN

- [ ] He creado el superusuario con `./create_admin.sh`
- [ ] He iniciado el servidor con `./run.sh`
- [ ] Puedo acceder a http://127.0.0.1:8000/
- [ ] Puedo acceder a http://127.0.0.1:8000/admin/
- [ ] He creado un usuario normal
- [ ] He compartido mi primera receta
- [ ] He puntuado una receta
- [ ] Mi perfil está personalizado

---

## 📚 DOCUMENTACIÓN ADICIONAL

Para más información, revisa:

- **README.md** - Documentación técnica completa
- **GUIA_USO.md** - Guía de uso detallada
- **INSTALACION.md** - Instalación avanzada

---

## 🎉 ¡LISTO!

Ya puedes:
- ✅ Compartir recetas
- ✅ Ver recetas de otros
- ✅ Puntuar y comentar
- ✅ Crear tu perfil
- ✅ Buscar y filtrar

**¡Diviértete compartiendo tus mejores recetas! 🍳👨‍🍳**

---

Si necesitas ayuda, ejecuta:
```bash
cd /workspaces/Recetas-Express/recetas_project
python manage.py shell
```

O revisa: `/workspaces/Recetas-Express/GUIA_USO.md`
