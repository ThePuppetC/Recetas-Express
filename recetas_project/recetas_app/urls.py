from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('recetas/', views.listar_recetas, name='listar_recetas'),
    path('recetas/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('recetas/crear/', views.crear_receta, name='crear_receta'),
    path('recetas/<int:pk>/editar/', views.editar_receta, name='editar_receta'),
    path('recetas/<int:pk>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('mis-recetas/', views.mis_recetas, name='mis_recetas'),
    path('recetas/<int:pk>/puntuar/', views.puntuar_receta, name='puntuar_receta'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('categorias/', views.categorias_view, name='categorias'),
    path('categorias/<str:slug>/', views.categorias_view, name='categoria_detalle'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
