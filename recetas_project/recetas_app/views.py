from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

from .models import Receta, Puntuacion, Categoria, PerfilUsuario
from .forms import RegistroForm, LoginForm, RecetaForm, PuntuacionForm, PerfilUsuarioForm, BusquedaForm


def inicio(request):
    """Página de inicio con recetas populares"""
    recetas = Receta.objects.all().annotate(
        promedio=Avg('puntuaciones__puntuacion'),
        total_puntuaciones=Count('puntuaciones')
    ).order_by('-creada_en')[:12]
    
    categorias = Categoria.objects.all()
    
    context = {
        'recetas': recetas,
        'categorias': categorias,
    }
    return render(request, 'recetas_app/inicio.html', context)


def listar_recetas(request):
    """Lista todas las recetas con filtros"""
    form = BusquedaForm(request.GET)
    recetas = Receta.objects.all().annotate(
        promedio=Avg('puntuaciones__puntuacion'),
        total_puntuaciones=Count('puntuaciones')
    )
    
    # Búsqueda
    if request.GET.get('busqueda'):
        busqueda = request.GET.get('busqueda')
        recetas = recetas.filter(
            Q(titulo__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(ingredientes__icontains=busqueda)
        )
    
    # Filtro por categoría
    if request.GET.get('categoria'):
        recetas = recetas.filter(categoria_id=request.GET.get('categoria'))
    
    # Filtro por dificultad
    if request.GET.get('dificultad'):
        recetas = recetas.filter(dificultad=request.GET.get('dificultad'))
    
    # Filtro por tiempo
    if request.GET.get('tiempo_max'):
        try:
            tiempo = int(request.GET.get('tiempo_max'))
            recetas = recetas.filter(tiempo_preparacion__lte=tiempo)
        except ValueError:
            pass
    
    recetas = recetas.order_by('-creada_en')
    
    # Paginación
    paginator = Paginator(recetas, 12)
    page = request.GET.get('page')
    recetas = paginator.get_page(page)
    
    context = {
        'recetas': recetas,
        'form': form,
    }
    return render(request, 'recetas_app/listar_recetas.html', context)


def detalle_receta(request, pk):
    """Detalle completo de una receta"""
    receta = get_object_or_404(Receta, pk=pk)
    puntuaciones = receta.puntuaciones.all().order_by('-creada_en')
    promedio = receta.promedio_puntuacion()
    
    puedo_puntuar = False
    mi_puntuacion = None
    
    if request.user.is_authenticated:
        puedo_puntuar = not receta.puntuaciones.filter(usuario=request.user).exists()
        mi_puntuacion = receta.puntuaciones.filter(usuario=request.user).first()
    
    form = PuntuacionForm() if puedo_puntuar else None
    
    context = {
        'receta': receta,
        'puntuaciones': puntuaciones,
        'promedio': promedio,
        'total_puntuaciones': receta.total_puntuaciones(),
        'puedo_puntuar': puedo_puntuar,
        'mi_puntuacion': mi_puntuacion,
        'form': form,
    }
    return render(request, 'recetas_app/detalle_receta.html', context)


@login_required
def crear_receta(request):
    """Crear una nueva receta"""
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            messages.success(request, '¡Receta creada exitosamente!')
            return redirect('detalle_receta', pk=receta.pk)
    else:
        form = RecetaForm()
    
    context = {'form': form}
    return render(request, 'recetas_app/crear_receta.html', context)


@login_required
def editar_receta(request, pk):
    """Editar una receta existente"""
    receta = get_object_or_404(Receta, pk=pk, autor=request.user)
    
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Receta actualizada!')
            return redirect('detalle_receta', pk=receta.pk)
    else:
        form = RecetaForm(instance=receta)
    
    context = {'form': form, 'receta': receta}
    return render(request, 'recetas_app/editar_receta.html', context)


@login_required
def eliminar_receta(request, pk):
    """Eliminar una receta"""
    receta = get_object_or_404(Receta, pk=pk, autor=request.user)
    
    if request.method == 'POST':
        receta.delete()
        messages.success(request, '¡Receta eliminada!')
        return redirect('mis_recetas')
    
    context = {'receta': receta}
    return render(request, 'recetas_app/confirmar_eliminar.html', context)


@login_required
def mis_recetas(request):
    """Recetas del usuario autenticado"""
    recetas = Receta.objects.filter(autor=request.user).annotate(
        promedio=Avg('puntuaciones__puntuacion'),
        total_puntuaciones=Count('puntuaciones')
    ).order_by('-creada_en')
    
    paginator = Paginator(recetas, 12)
    page = request.GET.get('page')
    recetas = paginator.get_page(page)
    
    context = {'recetas': recetas}
    return render(request, 'recetas_app/mis_recetas.html', context)


@login_required
def puntuar_receta(request, pk):
    """Puntuar una receta"""
    receta = get_object_or_404(Receta, pk=pk)
    
    if request.user == receta.autor:
        messages.error(request, 'No puedes puntuar tu propia receta')
        return redirect('detalle_receta', pk=pk)
    
    if request.method == 'POST':
        form = PuntuacionForm(request.POST)
        if form.is_valid():
            puntuacion = form.save(commit=False)
            puntuacion.receta = receta
            puntuacion.usuario = request.user
            
            # Si el usuario ya puntuó, actualizar
            existing = Puntuacion.objects.filter(receta=receta, usuario=request.user)
            if existing.exists():
                existing.update(
                    puntuacion=puntuacion.puntuacion,
                    comentario=puntuacion.comentario
                )
                messages.success(request, '¡Calificación actualizada!')
            else:
                puntuacion.save()
                messages.success(request, '¡Gracias por calificar!')
            
            return redirect('detalle_receta', pk=pk)
    else:
        form = PuntuacionForm()
    
    context = {
        'receta': receta,
        'form': form,
    }
    return render(request, 'recetas_app/puntuar_receta.html', context)


def perfil_usuario(request, username):
    """Perfil público de un usuario"""
    usuario = get_object_or_404(User, username=username)
    perfil = PerfilUsuario.objects.get_or_create(usuario=usuario)[0]
    
    recetas = Receta.objects.filter(autor=usuario).annotate(
        promedio=Avg('puntuaciones__puntuacion'),
        total_puntuaciones=Count('puntuaciones')
    ).order_by('-creada_en')
    
    context = {
        'perfil_usuario': usuario,
        'perfil': perfil,
        'recetas': recetas[:6],
        'es_mi_perfil': request.user == usuario,
    }
    return render(request, 'recetas_app/perfil_usuario.html', context)


@login_required
def editar_perfil(request):
    """Editar el perfil del usuario autenticado"""
    perfil = PerfilUsuario.objects.get_or_create(usuario=request.user)[0]
    
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado!')
            return redirect('perfil_usuario', username=request.user.username)
    else:
        form = PerfilUsuarioForm(instance=perfil)
    
    context = {'form': form}
    return render(request, 'recetas_app/editar_perfil.html', context)


def categorias_view(request, slug=None):
    """Ver recetas por categoría"""
    categorias = Categoria.objects.all()
    
    if slug:
        categoria = get_object_or_404(Categoria, nombre=slug)
        recetas = Receta.objects.filter(categoria=categoria).annotate(
            promedio=Avg('puntuaciones__puntuacion'),
            total_puntuaciones=Count('puntuaciones')
        ).order_by('-creada_en')
    else:
        categoria = None
        recetas = None
    
    context = {
        'categorias': categorias,
        'categoria_seleccionada': categoria,
        'recetas': recetas,
    }
    return render(request, 'recetas_app/categorias.html', context)


def registro(request):
    """Registro de nuevo usuario"""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            PerfilUsuario.objects.create(usuario=usuario)
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Bienvenido {username}! Por favor inicia sesión')
            return redirect('login')
    else:
        form = RegistroForm()
    
    context = {'form': form}
    return render(request, 'recetas_app/registro.html', context)


def login_view(request):
    """Login de usuario"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'recetas_app/login.html', context)


@login_required
def logout_view(request):
    """Logout de usuario"""
    logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect('home')
