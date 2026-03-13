from django.urls import path

from . import views

app_name = "hoteleria"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("hoteles/", views.HotelListView.as_view(), name="hotel_list"),
    path("hoteles/nuevo/", views.HotelCreateView.as_view(), name="hotel_create"),
    path("hoteles/<int:pk>/editar/", views.HotelUpdateView.as_view(), name="hotel_update"),
    path("hoteles/<int:pk>/eliminar/", views.HotelDeleteView.as_view(), name="hotel_delete"),
    path("tipos-habitacion/", views.TipoHabitacionListView.as_view(), name="tipohabitacion_list"),
    path("tipos-habitacion/nuevo/", views.TipoHabitacionCreateView.as_view(), name="tipohabitacion_create"),
    path(
        "tipos-habitacion/<int:pk>/editar/",
        views.TipoHabitacionUpdateView.as_view(),
        name="tipohabitacion_update",
    ),
    path(
        "tipos-habitacion/<int:pk>/eliminar/",
        views.TipoHabitacionDeleteView.as_view(),
        name="tipohabitacion_delete",
    ),
    path("estados/", views.EstadoListView.as_view(), name="estado_list"),
    path("estados/nuevo/", views.EstadoCreateView.as_view(), name="estado_create"),
    path("estados/<int:pk>/editar/", views.EstadoUpdateView.as_view(), name="estado_update"),
    path("estados/<int:pk>/eliminar/", views.EstadoDeleteView.as_view(), name="estado_delete"),
    path("administradores/", views.AdministradorListView.as_view(), name="administrador_list"),
    path(
        "administradores/nuevo/",
        views.AdministradorCreateView.as_view(),
        name="administrador_create",
    ),
    path(
        "administradores/<int:pk>/editar/",
        views.AdministradorUpdateView.as_view(),
        name="administrador_update",
    ),
    path(
        "administradores/<int:pk>/eliminar/",
        views.AdministradorDeleteView.as_view(),
        name="administrador_delete",
    ),
    path("recepcionistas/", views.RecepcionistaListView.as_view(), name="recepcionista_list"),
    path(
        "recepcionistas/nuevo/",
        views.RecepcionistaCreateView.as_view(),
        name="recepcionista_create",
    ),
    path(
        "recepcionistas/<int:pk>/editar/",
        views.RecepcionistaUpdateView.as_view(),
        name="recepcionista_update",
    ),
    path(
        "recepcionistas/<int:pk>/eliminar/",
        views.RecepcionistaDeleteView.as_view(),
        name="recepcionista_delete",
    ),
    path("clientes/", views.ClienteListView.as_view(), name="cliente_list"),
    path("clientes/nuevo/", views.ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/<int:pk>/editar/", views.ClienteUpdateView.as_view(), name="cliente_update"),
    path("clientes/<int:pk>/eliminar/", views.ClienteDeleteView.as_view(), name="cliente_delete"),
    path("habituales/", views.HabitualListView.as_view(), name="habitual_list"),
    path("habituales/nuevo/", views.HabitualCreateView.as_view(), name="habitual_create"),
    path("habituales/<int:pk>/editar/", views.HabitualUpdateView.as_view(), name="habitual_update"),
    path("habituales/<int:pk>/eliminar/", views.HabitualDeleteView.as_view(), name="habitual_delete"),
    path("esporadicos/", views.EsporadicoListView.as_view(), name="esporadico_list"),
    path("esporadicos/nuevo/", views.EsporadicoCreateView.as_view(), name="esporadico_create"),
    path("esporadicos/<int:pk>/editar/", views.EsporadicoUpdateView.as_view(), name="esporadico_update"),
    path("esporadicos/<int:pk>/eliminar/", views.EsporadicoDeleteView.as_view(), name="esporadico_delete"),
    path("habitaciones/", views.HabitacionListView.as_view(), name="habitacion_list"),
    path("habitaciones/nuevo/", views.HabitacionCreateView.as_view(), name="habitacion_create"),
    path(
        "habitaciones/<str:pk>/editar/",
        views.HabitacionUpdateView.as_view(),
        name="habitacion_update",
    ),
    path(
        "habitaciones/<str:pk>/eliminar/",
        views.HabitacionDeleteView.as_view(),
        name="habitacion_delete",
    ),
    path("reservas/", views.ReservaListView.as_view(), name="reserva_list"),
    path("reservas/nuevo/", views.ReservaCreateView.as_view(), name="reserva_create"),
    path("reservas/<int:pk>/editar/", views.ReservaUpdateView.as_view(), name="reserva_update"),
    path("reservas/<int:pk>/eliminar/", views.ReservaDeleteView.as_view(), name="reserva_delete"),
]
