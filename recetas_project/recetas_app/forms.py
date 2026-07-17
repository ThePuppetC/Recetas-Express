from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Receta, Puntuacion, PerfilUsuario, Categoria


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, label='Nombre')
    last_name = forms.CharField(max_length=30, required=False, label='Apellido')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu usuario'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu contraseña'})
    )


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones', 
                  'tiempo_preparacion', 'tiempo_coccion', 'porciones', 'dificultad', 
                  'categoria', 'imagen']
        labels = {
            'titulo': 'Título de la receta',
            'descripcion': 'Descripción',
            'ingredientes': 'Ingredientes (uno por línea)',
            'instrucciones': 'Instrucciones (uno por línea)',
            'tiempo_preparacion': 'Tiempo de preparación (minutos)',
            'tiempo_coccion': 'Tiempo de cocción (minutos)',
            'porciones': 'Número de porciones',
            'dificultad': 'Nivel de dificultad',
            'categoria': 'Categoría',
            'imagen': 'Imagen de la receta',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la receta'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe tu receta'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Ingrediente 1\nIngrediente 2\n...'}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Paso 1\nPaso 2\n...'}),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'tiempo_coccion': forms.NumberInput(attrs={'class': 'form-control'}),
            'porciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'dificultad': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }


class PuntuacionForm(forms.ModelForm):
    class Meta:
        model = Puntuacion
        fields = ['puntuacion', 'comentario']
        labels = {
            'puntuacion': 'Calificación (1-5 estrellas)',
            'comentario': 'Tu comentario',
        }
        widgets = {
            'puntuacion': forms.RadioSelect(choices=[(i, f'{i} ⭐') for i in range(1, 6)], attrs={'class': 'form-check-input'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Cuéntanos tu opinión sobre esta receta...'}),
        }


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['bio', 'foto_perfil', 'ciudad', 'pais', 'preferencias_dieteticas']
        labels = {
            'bio': 'Biografía',
            'foto_perfil': 'Foto de perfil',
            'ciudad': 'Ciudad',
            'pais': 'País',
            'preferencias_dieteticas': 'Preferencias dietéticas',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Cuéntanos sobre ti...'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu ciudad'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu país'}),
            'preferencias_dieteticas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Vegetariano, Sin gluten'}),
        }


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar recetas express...',
            'type': 'search'
        })
    )
    categoria = forms.ModelChoiceField(
        label='Categoría',
        required=False,
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    dificultad = forms.ChoiceField(
        label='Dificultad',
        required=False,
        choices=[('', 'Todas')] + Receta.DIFICULTAD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tiempo_max = forms.IntegerField(
        label='Tiempo máximo (min)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '30'})
    )
