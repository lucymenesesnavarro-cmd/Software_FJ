"""Administración de reservas y registro de eventos."""
import logging
from excepciones import ReservaError, ErrorSistema

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

class Reserva:
    """Relaciona un cliente con un servicio y controla su estado."""

    contador = 0

    def __init__(self, cliente, servicio, duracion):
        if cliente is None or servicio is None:
            raise ReservaError("La reserva requiere un cliente y un servicio.")
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero.")
        Reserva.contador += 1
        self.codigo = f"R-{Reserva.contador:03d}"
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self, impuesto=0.19, descuento=0.0):
        try:
            if self.estado != "Pendiente":
                raise ReservaError("Solo se pueden confirmar reservas pendientes.")
            total = self.servicio.calcular_costo(self.duracion, impuesto, descuento)
        except ErrorSistema as error:
            logging.exception("No fue posible confirmar la reserva %s", self.codigo)
            raise ReservaError(f"Error al confirmar la reserva: {error}") from error
        else:
            self.estado = "Confirmada"
            logging.info("Reserva %s confirmada. Total: $%.2f", self.codigo, total)
            return total
        finally:
            logging.info("Finalizó el intento de confirmación de %s", self.codigo)

    def cancelar(self):
        try:
            if self.estado != "Confirmada" and self.estado != "Pendiente":
                raise ReservaError("La reserva no se puede cancelar en su estado actual.")
            self.estado = "Cancelada"
            logging.info("Reserva %s cancelada.", self.codigo)
            return True
        except ReservaError:
            logging.exception("Error al cancelar la reserva %s", self.codigo)
            raise

    def procesar(self):
        if self.estado != "Confirmada":
            raise ReservaError("La reserva debe estar confirmada para procesarse.")
        self.estado = "Procesada"
        logging.info("Reserva %s procesada correctamente.", self.codigo)
        return self.estado
