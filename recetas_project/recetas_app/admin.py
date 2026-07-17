from django.contrib import admin
from .models import Categoria, Receta, Puntuacion, PerfilUsuario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'total_recetas']
    search_fields = ['nombre']
    
    def total_recetas(self, obj):
        return obj.recetas.count()
    total_recetas.short_description = 'Total de recetas'


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'dificultad', 'tiempo_total', 'promedio_puntuacion', 'creada_en']
    list_filter = ['categoria', 'dificultad', 'creada_en']
    search_fields = ['titulo', 'autor__username']
    readonly_fields = ['creada_en', 'actualizada_en', 'promedio_puntuacion', 'total_puntuaciones']
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'descripcion', 'autor', 'categoria', 'imagen')
        }),
        ('Detalles de la receta', {
            'fields': ('ingredientes', 'instrucciones', 'dificultad', 'porciones')
        }),
        ('Tiempos', {
            'fields': ('tiempo_preparacion', 'tiempo_coccion')
        }),
        ('Estadísticas', {
            'fields': ('promedio_puntuacion', 'total_puntuaciones', 'creada_en', 'actualizada_en'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Puntuacion)
class PuntuacionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'receta', 'puntuacion', 'creada_en']
    list_filter = ['puntuacion', 'creada_en']
    search_fields = ['usuario__username', 'receta__titulo']
    readonly_fields = ['creada_en', 'actualizada_en']


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'ciudad', 'pais', 'total_recetas', 'total_puntuaciones_recibidas']
    list_filter = ['pais', 'ciudad']
    search_fields = ['usuario__username']
    readonly_fields = ['creado_en', 'actualizado_en']
    
    def total_recetas(self, obj):
        return obj.total_recetas
    total_recetas.short_description = 'Recetas publicadas'
    
    def total_puntuaciones_recibidas(self, obj):
        return obj.total_puntuaciones_recibidas
    total_puntuaciones_recibidas.short_description = 'Puntuaciones recibidas'
