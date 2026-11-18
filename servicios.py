"""Servicios ofrecidos por Software FJ."""
from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(ABC):
    """Clase abstracta para los servicios disponibles."""

    def __init__(self, codigo, nombre, tarifa, disponible=True):
        if not codigo or not nombre:
            raise DatoInvalidoError("El código y el nombre del servicio son obligatorios.")
        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise DatoInvalidoError("La tarifa debe ser un número mayor que cero.")
        self.codigo = str(codigo)
        self.nombre = nombre
        self.tarifa = float(tarifa)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.nombre} no está disponible.")

    @abstractmethod
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        """Calcula el costo; los parámetros opcionales permiten distintas variantes de uso."""
        raise NotImplementedError

    @abstractmethod
    def describir(self):
        raise NotImplementedError


class ReservaSala(Servicio):
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        self.validar_disponibilidad()
        validar_cantidad(cantidad)
        return aplicar_ajustes(self.tarifa * cantidad, impuesto, descuento)

    def describir(self):
        return f"Reserva de sala por hora: {self.nombre}"


class AlquilerEquipo(Servicio):
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        self.validar_disponibilidad()
        validar_cantidad(cantidad)
        return aplicar_ajustes(self.tarifa * cantidad, impuesto, descuento)

    def describir(self):
        return f"Alquiler de equipo por día: {self.nombre}"


class Asesoria(Servicio):
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        self.validar_disponibilidad()
        validar_cantidad(cantidad)
        return aplicar_ajustes(self.tarifa * cantidad, impuesto, descuento)

    def describir(self):
        return f"Asesoría especializada: {self.nombre}"


def validar_cantidad(cantidad):
    if not isinstance(cantidad, (int, float)) or cantidad <= 0:
        raise DatoInvalidoError("La duración o cantidad debe ser mayor que cero.")


def aplicar_ajustes(subtotal, impuesto, descuento):
    if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 1:
        raise DatoInvalidoError("El impuesto debe expresarse entre 0 y 1.")
    if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 1:
        raise DatoInvalidoError("El descuento debe expresarse entre 0 y 1.")
    total_con_descuento = subtotal * (1 - descuento)
    return round(total_con_descuento * (1 + impuesto), 2)
