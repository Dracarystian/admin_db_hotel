from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .forms import (
	AdministradorForm,
	ClienteForm,
	EsporadicoForm,
	EstadoForm,
	HabitacionForm,
	HabitualForm,
	HotelForm,
	RecepcionistaForm,
	ReservaForm,
	TipoHabitacionForm,
)
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


class HomeView(TemplateView):
	template_name = "hoteleria/home.html"


class BaseListView(ListView):
	template_name = "hoteleria/generic_list.html"
	context_object_name = "objetos"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["titulo"] = self.model._meta.verbose_name_plural.title()
		context["modelo"] = self.model._meta.model_name
		return context


class BaseCreateView(CreateView):
	template_name = "hoteleria/generic_form.html"

	def get_success_url(self):
		return reverse_lazy(f"hoteleria:{self.model._meta.model_name}_list")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["titulo"] = f"Crear {self.model._meta.verbose_name.title()}"
		context["modelo"] = self.model._meta.model_name
		return context


class BaseUpdateView(UpdateView):
	template_name = "hoteleria/generic_form.html"

	def get_success_url(self):
		return reverse_lazy(f"hoteleria:{self.model._meta.model_name}_list")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["titulo"] = f"Editar {self.model._meta.verbose_name.title()}"
		context["modelo"] = self.model._meta.model_name
		return context


class BaseDeleteView(DeleteView):
	template_name = "hoteleria/generic_confirm_delete.html"

	def get_success_url(self):
		return reverse_lazy(f"hoteleria:{self.model._meta.model_name}_list")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["titulo"] = f"Eliminar {self.model._meta.verbose_name.title()}"
		context["modelo"] = self.model._meta.model_name
		return context


class HotelListView(BaseListView):
	model = Hotel


class HotelCreateView(BaseCreateView):
	model = Hotel
	form_class = HotelForm


class HotelUpdateView(BaseUpdateView):
	model = Hotel
	form_class = HotelForm


class HotelDeleteView(BaseDeleteView):
	model = Hotel


class TipoHabitacionListView(BaseListView):
	model = TipoHabitacion


class TipoHabitacionCreateView(BaseCreateView):
	model = TipoHabitacion
	form_class = TipoHabitacionForm


class TipoHabitacionUpdateView(BaseUpdateView):
	model = TipoHabitacion
	form_class = TipoHabitacionForm


class TipoHabitacionDeleteView(BaseDeleteView):
	model = TipoHabitacion


class EstadoListView(BaseListView):
	model = Estado


class EstadoCreateView(BaseCreateView):
	model = Estado
	form_class = EstadoForm


class EstadoUpdateView(BaseUpdateView):
	model = Estado
	form_class = EstadoForm


class EstadoDeleteView(BaseDeleteView):
	model = Estado


class AdministradorListView(BaseListView):
	model = Administrador


class AdministradorCreateView(BaseCreateView):
	model = Administrador
	form_class = AdministradorForm


class AdministradorUpdateView(BaseUpdateView):
	model = Administrador
	form_class = AdministradorForm


class AdministradorDeleteView(BaseDeleteView):
	model = Administrador


class RecepcionistaListView(BaseListView):
	model = Recepcionista


class RecepcionistaCreateView(BaseCreateView):
	model = Recepcionista
	form_class = RecepcionistaForm


class RecepcionistaUpdateView(BaseUpdateView):
	model = Recepcionista
	form_class = RecepcionistaForm


class RecepcionistaDeleteView(BaseDeleteView):
	model = Recepcionista


class ClienteListView(BaseListView):
	model = Cliente


class ClienteCreateView(BaseCreateView):
	model = Cliente
	form_class = ClienteForm


class ClienteUpdateView(BaseUpdateView):
	model = Cliente
	form_class = ClienteForm


class ClienteDeleteView(BaseDeleteView):
	model = Cliente


class HabitualListView(BaseListView):
	model = Habitual


class HabitualCreateView(BaseCreateView):
	model = Habitual
	form_class = HabitualForm


class HabitualUpdateView(BaseUpdateView):
	model = Habitual
	form_class = HabitualForm


class HabitualDeleteView(BaseDeleteView):
	model = Habitual


class EsporadicoListView(BaseListView):
	model = Esporadico


class EsporadicoCreateView(BaseCreateView):
	model = Esporadico
	form_class = EsporadicoForm


class EsporadicoUpdateView(BaseUpdateView):
	model = Esporadico
	form_class = EsporadicoForm


class EsporadicoDeleteView(BaseDeleteView):
	model = Esporadico


class HabitacionListView(BaseListView):
	model = Habitacion


class HabitacionCreateView(BaseCreateView):
	model = Habitacion
	form_class = HabitacionForm


class HabitacionUpdateView(BaseUpdateView):
	model = Habitacion
	form_class = HabitacionForm


class HabitacionDeleteView(BaseDeleteView):
	model = Habitacion


class ReservaListView(BaseListView):
	model = Reserva


class ReservaCreateView(BaseCreateView):
	model = Reserva
	form_class = ReservaForm


class ReservaUpdateView(BaseUpdateView):
	model = Reserva
	form_class = ReservaForm


class ReservaDeleteView(BaseDeleteView):
	model = Reserva
