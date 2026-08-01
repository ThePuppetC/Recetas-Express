# Recetas Express - Contexto para Desarrollo

## 🎯 Qué es
App Django 5.x para compartir recetas. Usuarios autenticados crean, califican y comentan recetas.

## 📦 Stack
- **Backend**: Django 5.x, SQLite3
- **Frontend**: Bootstrap 5.3, Vanilla JS, HTML5 templates
- **Python**: 3.12, venv configurado
- **Hosting**: Disponible en /workspaces/Recetas-Express

## 🏗️ Estructura Clave
```
recetas_project/
  ├── recetas_app/
  │   ├── models.py → Categoria, Receta, Puntuacion, PerfilUsuario
  │   ├── views.py → Lógica principal (queries optimizadas)
  │   ├── forms.py → RegistroForm, RecetaForm, PuntuacionForm
  │   ├── image_utils.py → WebP, resize, múltiples tamaños
  │   ├── validators.py → Validar MIME, tamaño, ext (5MB máx)
  │   ├── templates/ → HTML templates
  │   └── static/css/style.css → Responsive (1200px, 992px, 768px, 576px)
  ├── settings.py → DEBUG=True, ALLOWED_HOSTS=*
  ├── manage.py
  └── db.sqlite3
```

## 🔑 Características Actuales
✅ **Auth**: Registro, login, perfil con username dominante  
✅ **Recetas**: CRUD completo, búsqueda, filtros  
✅ **Rating**: UI estrellas (5 estrellas en línea), hover preview, comentarios  
✅ **Accesibilidad**: Botón flotante voz (silenciable)  
✅ **Performance**: select_related + prefetch_related (sin N+1)  
✅ **Seguridad**: Validar uploads, MIME check  
✅ **Responsive**: Mobile first, adapta desktop/tablet/móvil  

## 📊 Base de Datos - Campos Imagen
```python
imagen = ImageField(upload_to='recetas/images/%Y/%m/%d/')
imagen_numero = IntegerField()  # contador secuencial
imagen_ancho = IntegerField()
imagen_alto = IntegerField()
imagen_size_kb = IntegerField()
```
*Nota: WebP processing está en `image_utils.py` pero aún no integrado en views*

## 🚀 Comandos Útiles
```bash
# Desarrollo
cd /workspaces/Recetas-Express
python recetas_project/manage.py runserver

# Tests (3 tests passing)
python recetas_project/manage.py test recetas_app.tests --verbosity 2

# Migraciones
python recetas_project/manage.py makemigrations recetas_app
python recetas_project/manage.py migrate

# Admin
python recetas_project/manage.py createsuperuser
# Acceso: /admin/
```

## ⚠️ Tareas Pendientes
1. **Integrar WebP processing**: `image_utils.process_recipe_image()` → views `crear_receta()` y `editar_receta()`
2. **Lazy loading imágenes**: Agregar `loading="lazy"` en templates
3. **Static files compression**: `python manage.py collectstatic`
4. **Email verification**: Sistema de activación (optional)
5. **Rate limiting**: Proteger uploads masivos (optional)

## 🔧 Cómo Ayudar
- **Bug fix**: Test antes/después en `recetas_app/tests.py`
- **Feature nueva**: Agregar en modelo → form → view → template
- **Performance**: Usar Django Debug Toolbar para queries
- **CSS/Responsive**: Media queries en `style.css` (breakpoints: 1200, 992, 768, 576px)

## 📝 Testing
```bash
# Comando estándar
python recetas_project/manage.py test recetas_app.tests --verbosity 2

# Resultado esperado: 3/3 tests passing
- test_registro_permite_contraseñas_simples
- test_otro_usuario_puede_calificar_y_guardar_comentario
- test_el_menu_no_muestra_editar_perfil_en_la_barra_principal
```

## 🔗 URLs Principales
```
/                          → Inicio
/recetas/                  → Listar todas
/recetas/<id>/             → Detalle
/recetas/<id>/puntuar/     → Rating form
/categorias/               → Categorías
/@<username>/              → Perfil usuario
/registro/                 → Sign up
/login/                    → Sign in
/admin/                    → Panel (superuser)
```

## 🎨 Diseño
- Username siempre dominante (@usuario)
- Full name es secundario
- Rating: 5 estrellas en línea (sin duplicados)
- Responsive: mobile-first
- Colores: verde #2ecc71 (primary), amarillo #ffc107 (ratings)

## 💡 Tips
- No tocar `models.Puntuacion.Meta.unique_together` → previene doble rating
- `Receta.promedio_puntuacion()` → cached en vista si necesario
- Views usan `.select_related('categoria', 'autor')` → optimizado
- Imagen upload: máx 5MB, solo JPEG/PNG/GIF/WebP

## 📞 Estado del Proyecto
- Última actualización: 2026-08-01
- Última commit: `1df4bb4` - Responsive Design
- Ambiente: Development (DEBUG=True)
- BD: Migrations actualizadas

---
**Próximo paso típico**: Integrar WebP processing en views antes de producción.
