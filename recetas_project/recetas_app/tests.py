from django.test import TestCase

from .forms import RegistroForm


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
