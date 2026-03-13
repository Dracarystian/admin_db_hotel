from django.contrib import admin

from .models import (
	Administrador,
	Cliente,
	Esporadico,
	Estado,
	Habitacion,
	Habitual,
	Hotel,
	Recepcionista,
	Reserva,
	TipoHabitacion,
)

admin.site.register(Hotel)
admin.site.register(TipoHabitacion)
admin.site.register(Estado)
admin.site.register(Administrador)
admin.site.register(Recepcionista)
admin.site.register(Cliente)
admin.site.register(Habitual)
admin.site.register(Esporadico)
admin.site.register(Habitacion)
admin.site.register(Reserva)
