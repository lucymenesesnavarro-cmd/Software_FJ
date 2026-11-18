"""Punto de entrada: ejecuta diez operaciones demostrativas de Software FJ."""
import logging

from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import ErrorSistema, DatoInvalidoError, ReservaError


def ejecutar_pruebas():
    """Ejecuta casos válidos e inválidos y muestra un resumen de resultados."""
    clientes = []
    servicios = []
    reservas = []
    cliente1 = None
    sala = None
    reserva1 = None

    print("=" * 60)
    print(" SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 60)

    # Operación 1: registra un cliente con datos válidos.
    try:
        cliente1 = Cliente("C001", "Laura Gómez", "laura@gmail.com", "3001234567")
        clientes.append(cliente1)
        print("\n1. Cliente registrado:", cliente1.mostrar_informacion())
    except ErrorSistema as error:
        logging.exception("No se pudo completar la operación 1.")
        print("\n1. Error controlado:", error)

    # Operación 2: comprueba que se rechace un correo con formato incorrecto.
    try:
        Cliente("C002", "Carlos Pérez", "correo-invalido", "3101234567")
    except DatoInvalidoError as error:
        logging.exception("Operación 2: registro inválido de cliente.")
        print("\n2. Error controlado al registrar cliente:", error)

    # Operación 3: crea un servicio de reserva de sala.
    try:
        sala = ReservaSala("S001", "Sala de reuniones", 50000)
        servicios.append(sala)
        print("\n3. Servicio creado:", sala.describir())
    except ErrorSistema as error:
        logging.exception("No se pudo completar la operación 3.")
        print("\n3. Error controlado:", error)

    # Operación 4: crea un servicio de alquiler de equipo.
    try:
        equipo = AlquilerEquipo("E001", "Video proyector", 35000)
        servicios.append(equipo)
        print("\n4. Servicio creado:", equipo.describir())
    except ErrorSistema as error:
        logging.exception("No se pudo completar la operación 4.")
        print("\n4. Error controlado:", error)

    # Operación 5: crea un servicio de asesoría especializada.
    try:
        asesoria = Asesoria("A001", "Asesoría informática", 80000)
        servicios.append(asesoria)
        print("\n5. Servicio creado:", asesoria.describir())
    except ErrorSistema as error:
        logging.exception("No se pudo completar la operación 5.")
        print("\n5. Error controlado:", error)

    # Operación 6: intenta crear un servicio con tarifa negativa.
    try:
        ReservaSala("S002", "Sala inválida", -1000)
    except DatoInvalidoError as error:
        logging.exception("Operación 6: tarifa inválida.")
        print("\n6. Error controlado al crear servicio:", error)

    # Operación 7: crea y confirma una reserva válida.
    try:
        reserva1 = Reserva(cliente1, sala, 2)
        reservas.append(reserva1)
        total = reserva1.confirmar(impuesto=0.19)
        print(f"\n7. Reserva {reserva1.codigo} confirmada. Total: ${total:,.2f}")
    except ErrorSistema as error:
        logging.exception("No se pudo completar la operación 7.")
        print("\n7. Error controlado:", error)

    # Operación 8: comprueba el rechazo de una duración igual a cero.
    try:
        Reserva(cliente1, equipo, 0)
    except ReservaError as error:
        logging.exception("Operación 8: duración inválida.")
        print("\n8. Error controlado al crear reserva:", error)

    # Operación 9: intenta reservar un servicio que está suspendido.
    try:
        servicio_suspendido = Asesoria(
            "A002", "Asesoría suspendida", 60000, disponible=False
        )
        reserva_fallida = Reserva(cliente1, servicio_suspendido, 1)
        reserva_fallida.confirmar()
    except ErrorSistema as error:
        logging.exception("Operación 9: intento de reservar servicio no disponible.")
        print("\n9. Error controlado por disponibilidad:", error)

    # Operación 10: procesa la reserva y prueba una cancelación no permitida.
    try:
        print("\n10. Estado del procesamiento:", reserva1.procesar())
        reserva1.cancelar()
    except ReservaError as error:
        logging.exception("Operación 10: acción no permitida sobre la reserva.")
        print("   Error controlado:", error)
    finally:
        print("\nPruebas finalizadas. Revise logs.txt para consultar los eventos.")

    print("\nRESUMEN")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas correctamente: {len(reservas)}")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_pruebas()
