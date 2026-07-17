from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=50, default='🍳')
    
    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Receta(models.Model):
    DIFICULTAD_CHOICES = [
        ('Fácil', 'Fácil'),
        ('Medio', 'Medio'),
        ('Difícil', 'Difícil'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField(help_text="Escribe cada ingrediente en una línea separada")
    instrucciones = models.TextField(help_text="Escribe cada paso en una línea separada")
    tiempo_preparacion = models.IntegerField(help_text="En minutos")
    tiempo_coccion = models.IntegerField(help_text="En minutos", default=0)
    porciones = models.IntegerField(default=4)
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES, default='Fácil')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='recetas')
    imagen = models.ImageField(upload_to='recetas/%Y/%m/%d/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas')
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-creada_en']
        indexes = [
            models.Index(fields=['-creada_en']),
            models.Index(fields=['categoria']),
            models.Index(fields=['autor']),
        ]
    
    def __str__(self):
        return self.titulo
    
    def promedio_puntuacion(self):
        puntuaciones = self.puntuaciones.all()
        if not puntuaciones:
            return 0
        total = sum([p.puntuacion for p in puntuaciones])
        return round(total / len(puntuaciones), 1)
    
    def total_puntuaciones(self):
        return self.puntuaciones.count()
    
    @property
    def tiempo_total(self):
        return self.tiempo_preparacion + self.tiempo_coccion
    
    @property
    def ingredientes_list(self):
        return [ing.strip() for ing in self.ingredientes.split('\n') if ing.strip()]
    
    @property
    def instrucciones_list(self):
        return [ins.strip() for ins in self.instrucciones.split('\n') if ins.strip()]


class Puntuacion(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='puntuaciones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='puntuaciones_dadas')
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('receta', 'usuario')
        ordering = ['-creada_en']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.receta.titulo} ({self.puntuacion}★)"


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True, max_length=500)
    foto_perfil = models.ImageField(upload_to='perfiles/%Y/%m/%d/', null=True, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    preferencias_dieteticas = models.TextField(blank=True, help_text="Ej: Vegetariano, Sin gluten, etc.")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    @property
    def total_recetas(self):
        return self.usuario.recetas.count()
    
    @property
    def total_puntuaciones_recibidas(self):
        return Puntuacion.objects.filter(receta__autor=self.usuario).count()
