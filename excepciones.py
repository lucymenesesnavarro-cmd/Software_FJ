"""Excepciones personalizadas del sistema Software FJ."""

class ErrorSistema(Exception):
    """Error base para las operaciones del sistema."""

class DatoInvalidoError(ErrorSistema):
    """Se presenta cuando un dato no cumple las validaciones."""

class ServicioNoDisponibleError(ErrorSistema):
    """Se presenta cuando un servicio no está disponible."""

class ReservaError(ErrorSistema):
    """Se presenta cuando una reserva no puede procesarse."""
