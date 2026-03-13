from django.core.exceptions import ValidationError
from django.db import models


class Hotel(models.Model):
	nombre = models.CharField(max_length=150)
	direccion = models.CharField(max_length=255, blank=True)
	telefono = models.CharField(max_length=20, blank=True)
	habitacion_ocupada = models.IntegerField(default=0)
	habitacion_disponible = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Hotel"
		verbose_name_plural = "Hoteles"

	def __str__(self):
		return self.nombre


class TipoHabitacion(models.Model):
	tipo_habitacion = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Tipo de habitacion"
		verbose_name_plural = "Tipos de habitacion"

	def __str__(self):
		return self.tipo_habitacion


class Estado(models.Model):
	estado = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Estado"
		verbose_name_plural = "Estados"

	def __str__(self):
		return self.estado


class Administrador(models.Model):
	nombre_admin = models.CharField(max_length=150)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="administradores")

	class Meta:
		verbose_name = "Administrador"
		verbose_name_plural = "Administradores"

	def __str__(self):
		return self.nombre_admin


class Recepcionista(models.Model):
	nombre_recepcionista = models.CharField(max_length=150)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="recepcionistas")

	class Meta:
		verbose_name = "Recepcionista"
		verbose_name_plural = "Recepcionistas"

	def __str__(self):
		return self.nombre_recepcionista


class Cliente(models.Model):
	nombre = models.CharField(max_length=150)
	numero_documento = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=150, blank=True)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="clientes")

	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clientes"

	def __str__(self):
		return f"{self.nombre} ({self.numero_documento})"


class Habitual(models.Model):
	cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)
	descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	class Meta:
		verbose_name = "Cliente habitual"
		verbose_name_plural = "Clientes habituales"

	def __str__(self):
		return f"Habitual: {self.cliente.nombre}"


class Esporadico(models.Model):
	cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)

	class Meta:
		verbose_name = "Cliente esporadico"
		verbose_name_plural = "Clientes esporadicos"

	def __str__(self):
		return f"Esporadico: {self.cliente.nombre}"


class Habitacion(models.Model):
	numero_habitacion = models.CharField(max_length=50, primary_key=True)
	tipo_habitacion_texto = models.CharField(max_length=100, blank=True)
	tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.SET_NULL, null=True, blank=True)
	foto = models.TextField(blank=True)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="habitaciones")
	recepcionista = models.ForeignKey(
		Recepcionista,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name="habitaciones_asignadas",
	)
	administrador = models.ForeignKey(
		Administrador,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name="habitaciones_supervisadas",
	)

	class Meta:
		verbose_name = "Habitacion"
		verbose_name_plural = "Habitaciones"

	def __str__(self):
		return f"Hab. {self.numero_habitacion}"


class Reserva(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
	habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name="reservas")
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	dias_noches = models.IntegerField()
	nombre_cliente = models.CharField(max_length=150, blank=True)
	precio_total = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name = "Reserva"
		verbose_name_plural = "Reservas"

	def __str__(self):
		return f"Reserva #{self.pk} - {self.cliente.nombre}"

	def clean(self):
		if self.fecha_fin and self.fecha_inicio and self.fecha_fin <= self.fecha_inicio:
			raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

	def save(self, *args, **kwargs):
		if self.fecha_inicio and self.fecha_fin:
			self.dias_noches = (self.fecha_fin - self.fecha_inicio).days
		if self.cliente and not self.nombre_cliente:
			self.nombre_cliente = self.cliente.nombre
		super().save(*args, **kwargs)
