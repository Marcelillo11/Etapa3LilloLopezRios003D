import uuid
from django.db import models

# Create your models here.

class UsuarioEmpresa(models.Model):
	rutEmpresa = models.CharField(primary_key=True, max_length=10, help_text='Sin puntos, con guion')
	nombreEmpresa = models.CharField(max_length=50)
	direccionEmpresa = models.CharField(max_length=50)
	telefonoEmpresa = models.CharField(max_length=9)
	correoEmpresa = models.EmailField(max_length=50)
	ciudadEmpresa = models.CharField(max_length=50)
	comunaEmpresa = models.CharField(max_length=50)
	rubro = models.CharField(max_length=50)
	nombreRepresentante = models.CharField(max_length=50)
	rutRepresentante = models.CharField(max_length=10, help_text='Sin puntos, con guion')
	contraseñaEmpresa = models.CharField(max_length=50)

	def __str__(self):
		return self.nombreEmpresa

class UsuarioRepartidor(models.Model):
	rutRepartidor = models.CharField(primary_key=True, max_length=10, help_text='Sin puntos, con guion')
	nombreRepartidor = models.CharField(max_length=50)
	apellidosRepartidor = models.CharField(max_length=50)
	direccionRepartidor = models.CharField(max_length=50)
	telefonoRepartidor = models.CharField(max_length=9)
	correoRepartidor = models.EmailField(max_length=50)
	ciudadRepartidor = models.CharField(max_length=50)
	comunaRepartidor = models.CharField(max_length=50)
	contraseñaRepartidor = models.CharField(max_length=50)

	def __str__(self):
		return self.rutRepartidor

class Vehiculo(models.Model):
	patente = models.CharField(primary_key=True, max_length=6)
	usuarioR = models.ForeignKey(UsuarioRepartidor, on_delete=models.PROTECT)
	marca = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	año = models.IntegerField()

	def __str__(self):
		return self.patente

class Envios(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	usuarioE = models.ForeignKey(UsuarioEmpresa, on_delete=models.PROTECT)
	usuarioR = models.ForeignKey(UsuarioRepartidor, on_delete=models.PROTECT)
	direccionDestino = models.CharField(max_length=50)
	nombreDestino = models.CharField(max_length=50)
	rutDestino = models.CharField(max_length=10, help_text='Sin puntos, con guion')
	telefonoDestino = models.CharField(max_length=9)
	correoDestino = models.EmailField(max_length=50)
	fechaEnvio = models.DateField()
	fechaEstimadaEntrega = models.DateField()

	LOAN_STATUS = (
		('d', 'Despachado'),
		('t', 'En Transito'),
		('e', 'Entregado'),
		('w', 'En Espera'),
		('n', 'No se encuentra en domicilio')
	)

	estadoEnvio = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		help_text='Estado del Envío',
		default = 'w',
	)

	def __str__(self):
		return str(self.id)
