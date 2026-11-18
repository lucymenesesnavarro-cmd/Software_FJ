"""Entidades generales y clientes del sistema."""
from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError

class Entidad(ABC):
    """Clase abstracta que representa una entidad del sistema."""

    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise DatoInvalidoError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Devuelve la información principal de la entidad."""
        raise NotImplementedError


class Cliente(Entidad):
    """Representa un cliente con datos personales encapsulados."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise DatoInvalidoError("El correo electrónico no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        texto = str(valor).strip()
        if not texto.isdigit() or len(texto) < 7:
            raise DatoInvalidoError("El teléfono debe contener al menos 7 dígitos.")
        self._telefono = texto

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}"
