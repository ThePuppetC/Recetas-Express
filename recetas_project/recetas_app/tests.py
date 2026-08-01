from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import RegistroForm
from .models import Categoria, Puntuacion, Receta


class RegistroFormTests(TestCase):
    def test_registro_permite_contraseñas_simples(self):
        form = RegistroForm(
            data={
                'username': 'usuario1',
                'email': 'usuario1@example.com',
                'first_name': 'Usuario',
                'last_name': 'Prueba',
                'password1': '12345678',
                'password2': '12345678',
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertEqual(user.username, 'usuario1')
        self.assertTrue(user.check_password('12345678'))


class CalificacionTests(TestCase):
    def setUp(self):
        self.autor = User.objects.create_user('autor', 'autor@example.com', '12345678')
        self.usuario = User.objects.create_user('usuario', 'usuario@example.com', '12345678')
        self.categoria = Categoria.objects.create(nombre='Postres', descripcion='')
        self.imagen = SimpleUploadedFile('receta.jpg', b'fake-image', content_type='image/jpeg')
        self.receta = Receta.objects.create(
            titulo='Tarta',
            descripcion='Tarta de prueba',
            ingredientes='Harina',
            instrucciones='Mezclar',
            tiempo_preparacion=20,
            tiempo_coccion=10,
            porciones=4,
            dificultad='Fácil',
            categoria=self.categoria,
            imagen=self.imagen,
            autor=self.autor,
        )

    def test_otro_usuario_puede_calificar_y_guardar_comentario(self):
        self.client.force_login(self.usuario)
        response = self.client.post(
            f'/recetas/{self.receta.id}/puntuar/',
            {'puntuacion': '5', 'comentario': 'Muy rica'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Puntuacion.objects.filter(receta=self.receta, usuario=self.usuario).exists())
        puntuacion = Puntuacion.objects.get(receta=self.receta, usuario=self.usuario)
        self.assertEqual(puntuacion.puntuacion, 5)
        self.assertEqual(puntuacion.comentario, 'Muy rica')

    def test_el_menu_no_muestra_editar_perfil_en_la_barra_principal(self):
        self.client.force_login(self.usuario)
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Editar Perfil')
