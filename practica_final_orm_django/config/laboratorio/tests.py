from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Laboratorio


# Create your tests here.

class BaseDeDatosTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ 
        Se realiza testeo de la base de datos creando un objeto en el modelo laboratorio.
        """
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio 5', ciudad='Ciudad 5', pais='País 5')


    def test_model(self):
        """
        Se verifica que cada atributo del objeto creado existe dentro de la base de datos.
        """
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio 5')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad 5')
        self.assertEqual(self.laboratorio.pais, 'País 5')



class UrlTest(TestCase):


    def test_url(self):
        """ 
        Se realiza testeo de endpoint
        """
        response = self.client.get('/laboratorio/')
        self.assertEqual(response.status_code, 200)

    
    def test_url_por_nombre(self):
        """ 
        Se verifica que el nombre de la url está funcionando
        """
        response = self.client.get(reverse('laboratorios'))
        self.assertEqual(response.status_code, 200)


    def test_template(self):
        """
        Se verifica que el template responda al ser llamado
        """
        response = self.client.get(reverse('laboratorios'))
        self.assertTemplateUsed(response, 'laboratorios.html')

    
    def test_contenido_html(self):
        """ 
        Se comprueba que el contenido html de la vista coincida con lo que espero mostrar.
        """
        response = self.client.get(reverse('laboratorios'))
        self.assertContains(response, '<div class="container my-5 py-5">')
        self.assertNotContains(response, 'Equivocado')