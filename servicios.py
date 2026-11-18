"""Clases abstractas y especializadas para los servicios de Software FJ."""
from abc import ABC, abstractmethod
from typing import overload

from excepciones import DatoInvalidoError, ServicioNoDisponibleError


class Servicio(ABC):
    """Clase abstracta que define el comportamiento común de un servicio."""

    def __init__(self, codigo, nombre, tarifa, disponible=True):
        """Inicializa el servicio validando sus datos principales."""
        if not isinstance(codigo, str) or not codigo.strip():
            raise DatoInvalidoError("El código del servicio es obligatorio.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalidoError("El nombre del servicio es obligatorio.")
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise DatoInvalidoError("La tarifa debe ser un número mayor que cero.")
        if not isinstance(disponible, bool):
            raise DatoInvalidoError("La disponibilidad debe ser verdadera o falsa.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.tarifa = float(tarifa)
        self.disponible = disponible

    def validar_disponibilidad(self):
        """Impide calcular el costo de un servicio que no está disponible."""
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no está disponible."
            )

    @overload
    def calcular_costo(self, cantidad: float = 1) -> float:
        ...

    @overload
    def calcular_costo(
        self, cantidad: float, impuesto: float, descuento: float = 0.0
    ) -> float:
        ...

    @abstractmethod
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        """Calcula el costo con variantes de parámetros documentadas mediante overload."""
        raise NotImplementedError

    @abstractmethod
    def describir(self):
        """Devuelve la descripción específica del servicio."""
        raise NotImplementedError

    def _calcular_total(self, cantidad, impuesto, descuento):
        """Comparte la validación y el cálculo para las clases derivadas."""
        self.validar_disponibilidad()
        validar_cantidad(cantidad)
        return aplicar_ajustes(self.tarifa * cantidad, impuesto, descuento)


class ReservaSala(Servicio):
    """Servicio especializado para reservar salas por hora."""

    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        """Calcula el costo de las horas reservadas."""
        return self._calcular_total(cantidad, impuesto, descuento)

    def describir(self):
        """Describe el servicio de reserva de sala."""
        return f"Reserva de sala por hora: {self.nombre}"


class AlquilerEquipo(Servicio):
    """Servicio especializado para alquilar equipos por día."""

    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        """Calcula el costo de los días de alquiler."""
        return self._calcular_total(cantidad, impuesto, descuento)

    def describir(self):
        """Describe el servicio de alquiler de equipo."""
        return f"Alquiler de equipo por día: {self.nombre}"


class Asesoria(Servicio):
    """Servicio especializado para asesorías profesionales."""

    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        """Calcula el costo de las unidades de asesoría contratadas."""
        return self._calcular_total(cantidad, impuesto, descuento)

    def describir(self):
        """Describe el servicio de asesoría especializada."""
        return f"Asesoría especializada: {self.nombre}"


def validar_cantidad(cantidad):
    """Comprueba que la cantidad o duración sea un número positivo."""
    if (
        isinstance(cantidad, bool)
        or not isinstance(cantidad, (int, float))
        or cantidad <= 0
    ):
        raise DatoInvalidoError("La duración o cantidad debe ser mayor que cero.")


def aplicar_ajustes(subtotal, impuesto=0.0, descuento=0.0):
    """Aplica primero el descuento y después el impuesto al subtotal."""
    for nombre, valor in (("impuesto", impuesto), ("descuento", descuento)):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not 0 <= valor <= 1
        ):
            raise DatoInvalidoError(
                f"El {nombre} debe expresarse como una proporción entre 0 y 1."
            )

    total_con_descuento = subtotal * (1 - descuento)
    return round(total_con_descuento * (1 + impuesto), 2)
