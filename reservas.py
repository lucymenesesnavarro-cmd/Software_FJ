"""Administración de reservas y registro de eventos del sistema."""
import logging
from pathlib import Path

from excepciones import ErrorSistema, ReservaError

# El archivo de eventos se crea en la carpeta desde la que se ejecuta el programa.
logging.basicConfig(
    filename="registros.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


class Reserva:
    """Relaciona un cliente con un servicio y controla el estado de la reserva."""

    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    PROCESADA = "Procesada"
    contador = 0

    def __init__(self, cliente, servicio, duracion):
        """Crea una reserva después de comprobar sus datos obligatorios."""
        if cliente is None or servicio is None:
            raise ReservaError("La reserva requiere un cliente y un servicio.")
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ReservaError("La duración debe ser mayor que cero.")

        Reserva.contador += 1
        self.codigo = f"R-{Reserva.contador:03d}"
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = self.PENDIENTE
        logging.info("Se creó la reserva %s para el cliente %s.", self.codigo,
                     self.cliente.identificador)

    def confirmar(self, impuesto=0.19, descuento=0.0):
        """Confirma una reserva pendiente y devuelve el total calculado."""
        try:
            if self.estado != self.PENDIENTE:
                raise ReservaError("Solo se pueden confirmar reservas pendientes.")
            total = self.servicio.calcular_costo(
                self.duracion, impuesto, descuento
            )
        except ErrorSistema as error:
            logging.exception("No fue posible confirmar la reserva %s.", self.codigo)
            raise ReservaError(
                f"Error al confirmar la reserva: {error}"
            ) from error
        else:
            self.estado = self.CONFIRMADA
            logging.info("Reserva %s confirmada. Total: $%.2f", self.codigo, total)
            return total
        finally:
            logging.info("Finalizó el intento de confirmación de %s.", self.codigo)

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""
        try:
            if self.estado not in (self.PENDIENTE, self.CONFIRMADA):
                raise ReservaError(
                    "La reserva no se puede cancelar en su estado actual."
                )
            self.estado = self.CANCELADA
            logging.info("Reserva %s cancelada.", self.codigo)
            return True
        except ReservaError:
            logging.exception("Error al cancelar la reserva %s.", self.codigo)
            raise

    def procesar(self):
        """Marca como procesada una reserva que haya sido confirmada."""
        try:
            if self.estado != self.CONFIRMADA:
                raise ReservaError(
                    "La reserva debe estar confirmada para procesarse."
                )
            self.estado = self.PROCESADA
            logging.info("Reserva %s procesada correctamente.", self.codigo)
            return self.estado
        except ReservaError:
            logging.exception("Error al procesar la reserva %s.", self.codigo)
            raise
