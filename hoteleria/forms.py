from django import forms

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


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"


class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = "__all__"


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = "__all__"


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = "__all__"


class RecepcionistaForm(forms.ModelForm):
    class Meta:
        model = Recepcionista
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class HabitualForm(forms.ModelForm):
    class Meta:
        model = Habitual
        fields = "__all__"


class EsporadicoForm(forms.ModelForm):
    class Meta:
        model = Esporadico
        fields = "__all__"


class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = "__all__"


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"
