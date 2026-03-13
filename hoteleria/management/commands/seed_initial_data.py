from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from hoteleria.models import (
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


class Command(BaseCommand):
    help = "Carga datos iniciales e idempotentes para la aplicacion de hoteleria."

    @transaction.atomic
    def handle(self, *args, **options):
        hotel, _ = Hotel.objects.update_or_create(
            nombre="Hotel Neon",
            defaults={
                "direccion": "Av. Principal 123, Bogota",
                "telefono": "+57 601 5550101",
            },
        )

        estados = {}
        for nombre_estado in ["Disponible", "Ocupada", "Mantenimiento"]:
            estado, _ = Estado.objects.get_or_create(estado=nombre_estado)
            estados[nombre_estado] = estado

        tipos = {}
        for nombre_tipo in ["Sencilla", "Doble", "Suite", "Familiar"]:
            tipo, _ = TipoHabitacion.objects.get_or_create(tipo_habitacion=nombre_tipo)
            tipos[nombre_tipo] = tipo

        administrador, _ = Administrador.objects.update_or_create(
            nombre_admin="Administrador General",
            hotel=hotel,
        )

        recepcionista_1, _ = Recepcionista.objects.update_or_create(
            nombre_recepcionista="Laura Gomez",
            hotel=hotel,
        )
        recepcionista_2, _ = Recepcionista.objects.update_or_create(
            nombre_recepcionista="Carlos Perez",
            hotel=hotel,
        )

        habitaciones_config = [
            {
                "numero_habitacion": "101",
                "tipo": "Sencilla",
                "precio": Decimal("180000.00"),
                "estado": "Disponible",
                "recepcionista": recepcionista_1,
            },
            {
                "numero_habitacion": "102",
                "tipo": "Doble",
                "precio": Decimal("250000.00"),
                "estado": "Disponible",
                "recepcionista": recepcionista_1,
            },
            {
                "numero_habitacion": "201",
                "tipo": "Suite",
                "precio": Decimal("420000.00"),
                "estado": "Ocupada",
                "recepcionista": recepcionista_2,
            },
            {
                "numero_habitacion": "202",
                "tipo": "Familiar",
                "precio": Decimal("360000.00"),
                "estado": "Mantenimiento",
                "recepcionista": recepcionista_2,
            },
        ]

        habitaciones = {}
        for item in habitaciones_config:
            habitacion, _ = Habitacion.objects.update_or_create(
                numero_habitacion=item["numero_habitacion"],
                defaults={
                    "tipo_habitacion_texto": item["tipo"],
                    "tipo_habitacion": tipos[item["tipo"]],
                    "foto": "",
                    "precio": item["precio"],
                    "estado": estados[item["estado"]],
                    "hotel": hotel,
                    "recepcionista": item["recepcionista"],
                    "administrador": administrador,
                },
            )
            habitaciones[item["numero_habitacion"]] = habitacion

        cliente_habitual, _ = Cliente.objects.update_or_create(
            numero_documento="CC1001001001",
            defaults={
                "nombre": "Ana Torres",
                "email": "ana.torres@example.com",
                "hotel": hotel,
            },
        )
        Habitual.objects.update_or_create(
            cliente=cliente_habitual,
            defaults={"descuento": Decimal("10.00")},
        )
        Esporadico.objects.filter(cliente=cliente_habitual).delete()

        cliente_esporadico, _ = Cliente.objects.update_or_create(
            numero_documento="CC1001001002",
            defaults={
                "nombre": "Miguel Rojas",
                "email": "miguel.rojas@example.com",
                "hotel": hotel,
            },
        )
        Esporadico.objects.update_or_create(cliente=cliente_esporadico)
        Habitual.objects.filter(cliente=cliente_esporadico).delete()

        fecha_inicio = date.today()
        fecha_fin = fecha_inicio + timedelta(days=2)
        Reserva.objects.update_or_create(
            cliente=cliente_habitual,
            habitacion=habitaciones["201"],
            defaults={
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "dias_noches": 2,
                "nombre_cliente": cliente_habitual.nombre,
                "precio_total": Decimal("840000.00"),
            },
        )

        hotel.habitacion_ocupada = Habitacion.objects.filter(hotel=hotel, estado=estados["Ocupada"]).count()
        hotel.habitacion_disponible = Habitacion.objects.filter(hotel=hotel, estado=estados["Disponible"]).count()
        hotel.save(update_fields=["habitacion_ocupada", "habitacion_disponible"])

        self.stdout.write(self.style.SUCCESS("Datos iniciales cargados correctamente."))