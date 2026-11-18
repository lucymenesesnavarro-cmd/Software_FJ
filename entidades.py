"""Clases que representan las entidades generales y los clientes."""
from abc import ABC, abstractmethod
import re

from excepciones import DatoInvalidoError


class Entidad(ABC):
    """Clase abstracta base para las entidades del sistema."""

    def __init__(self, identificador):
        """Inicializa una entidad después de validar su identificador."""
        if not isinstance(identificador, str) or not identificador.strip():
            raise DatoInvalidoError("El identificador es obligatorio.")
        self._identificador = identificador.strip()

    @property
    def identificador(self):
        """Devuelve el identificador sin permitir modificarlo directamente."""
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Define el método que cada entidad debe implementar."""
        raise NotImplementedError


class Cliente(Entidad):
    """Representa un cliente y encapsula sus datos personales."""

    def __init__(self, identificador, nombre, correo, telefono):
        """Crea un cliente validando cada uno de sus datos."""
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        """Obtiene el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Valida y almacena el nombre del cliente."""
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def correo(self):
        """Obtiene el correo electrónico del cliente."""
        return self._correo

    @correo.setter
    def correo(self, valor):
        """Valida el formato básico del correo y lo normaliza."""
        if not isinstance(valor, str):
            raise DatoInvalidoError("El correo debe ser texto.")
        correo = valor.strip()
        patron = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        if not re.match(patron, correo):
            raise DatoInvalidoError("El correo electrónico no tiene un formato válido.")
        self._correo = correo.lower()

    @property
    def telefono(self):
        """Obtiene el teléfono del cliente."""
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        """Valida que el teléfono contenga al menos siete dígitos."""
        texto = str(valor).strip()
        if not texto.isdigit() or len(texto) < 7:
            raise DatoInvalidoError("El teléfono debe contener al menos 7 dígitos.")
        self._telefono = texto

    def mostrar_informacion(self):
        """Devuelve un resumen legible de los datos del cliente."""
        return (
            f"Cliente: {self.nombre} | Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
