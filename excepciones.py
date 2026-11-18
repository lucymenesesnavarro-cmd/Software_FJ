"""Excepciones personalizadas del sistema Software FJ."""


class ErrorSistema(Exception):
    """Clase base para los errores controlados de la aplicación."""


class DatoInvalidoError(ErrorSistema):
    """Indica que un dato recibido no cumple las reglas de validación."""


class ServicioNoDisponibleError(ErrorSistema):
    """Indica que se intentó utilizar un servicio suspendido o no disponible."""


class ReservaError(ErrorSistema):
    """Indica que una operación relacionada con una reserva no es válida."""
