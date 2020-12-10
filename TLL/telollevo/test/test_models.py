from django.test import TestCase
from telollevo.models import UsuarioEmpresa

class UsuarioEmpresaModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		UsuarioEmpresa.objects.create(rutEmpresa='12345678-9', nombreEmpresa='Test', direccionEmpresa='Test 123', telefonoEmpresa='912345678', correoEmpresa='test@test.cl', ciudadEmpresa='Santiago', comunaEmpresa='Maipu', rubro='Tecnologia', nombreRepresentante='Test Perez', rutRepresentante='12345678-9', contraseñaEmpresa='test123')
	
	def test_rutEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('rutEmpresa').verbose_name
		self.assertEquals(field_label,'rutEmpresa')

	def test_nombreEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('nombreEmpresa').verbose_name
		self.assertEquals(field_label,'nombreEmpresa')

	def test_direccionEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('direccionEmpresa').verbose_name
		self.assertEquals(field_label,'direccionEmpresa')

	def test_telefonoEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('telefonoEmpresa').verbose_name
		self.assertEquals(field_label,'telefonoEmpresa')

	def test_correoEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('correoEmpresa').verbose_name
		self.assertEquals(field_label,'correoEmpresa')

	def test_ciudadEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('ciudadEmpresa').verbose_name
		self.assertEquals(field_label,'ciudadEmpresa')

	def test_comunaEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('comunaEmpresa').verbose_name
		self.assertEquals(field_label,'comunaEmpresa')

	def test_rubro_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('rubro').verbose_name
		self.assertEquals(field_label,'rubro')

	def test_nombreRepresentante_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('nombreRepresentante').verbose_name
		self.assertEquals(field_label,'nombreRepresentante')

	def test_rutRepresentante_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('rutRepresentante').verbose_name
		self.assertEquals(field_label,'rutRepresentante')

	def test_contraseñaEmpresa_label(self):
		empresa = UsuarioEmpresa.objects.get(rutEmpresa='12345678-9')
		field_label = empresa._meta.get_field('contraseñaEmpresa').verbose_name
		self.assertEquals(field_label,'contraseñaEmpresa')

