"""Programa principal: demostración de Software FJ."""
import logging
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import ErrorSistema, DatoInvalidoError, ReservaError

def ejecutar_pruebas():
    clientes = []
    servicios = []
    reservas = []

    print("=" * 60)
    print(" SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 60)

    # Operación 1: registro válido de cliente.
    try:
        cliente1 = Cliente("C001", "Laura Gómez", "laura@gmail.com", "3001234567")
        clientes.append(cliente1)
        print("\n1. Cliente registrado:", cliente1.mostrar_informacion())
    except ErrorSistema as error:
        print("1. Error:", error)

    # Operación 2: intento de registro con correo inválido.
    try:
        Cliente("C002", "Carlos Pérez", "correo-invalido", "3101234567")
    except DatoInvalidoError as error:
        logging.exception("Registro inválido de cliente.")
        print("\n2. Error controlado al registrar cliente:", error)

    # Operación 3: creación de reserva de sala.
    try:
        sala = ReservaSala("S001", "Sala de reuniones", 50000)
        servicios.append(sala)
        print("\n3. Servicio creado:", sala.describir())
    except ErrorSistema as error:
        print("3. Error:", error)

    # Operación 4: creación de alquiler de equipo.
    try:
        equipo = AlquilerEquipo("E001", "Video proyector", 35000)
        servicios.append(equipo)
        print("\n4. Servicio creado:", equipo.describir())
    except ErrorSistema as error:
        print("4. Error:", error)

    # Operación 5: creación de asesoría.
    try:
        asesoria = Asesoria("A001", "Asesoría informática", 80000)
        servicios.append(asesoria)
        print("\n5. Servicio creado:", asesoria.describir())
    except ErrorSistema as error:
        print("5. Error:", error)

    # Operación 6: servicio con tarifa inválida.
    try:
        ReservaSala("S002", "Sala inválida", -1000)
    except DatoInvalidoError as error:
        logging.exception("Intento de crear servicio con tarifa inválida.")
        print("\n6. Error controlado al crear servicio:", error)

    # Operación 7: reserva válida y confirmación.
    try:
        reserva1 = Reserva(cliente1, sala, 2)
        reservas.append(reserva1)
        total = reserva1.confirmar(impuesto=0.19)
        print(f"\n7. Reserva {reserva1.codigo} confirmada. Total: ${total:,.2f}")
    except ErrorSistema as error:
        print("7. Error:", error)

    # Operación 8: intento de reserva con duración inválida.
    try:
        Reserva(cliente1, equipo, 0)
    except ReservaError as error:
        logging.exception("Intento de reserva con duración inválida.")
        print("\n8. Error controlado al crear reserva:", error)

    # Operación 9: servicio no disponible.
    try:
        servicio_suspendido = Asesoria("A002", "Asesoría suspendida", 60000, disponible=False)
        reserva_fallida = Reserva(cliente1, servicio_suspendido, 1)
        reserva_fallida.confirmar()
    except ErrorSistema as error:
        logging.exception("Intento de reservar un servicio no disponible.")
        print("\n9. Error controlado por disponibilidad:", error)

    # Operación 10: procesar y luego cancelar una reserva ya procesada.
    try:
        print("\n10. Estado del procesamiento:", reserva1.procesar())
        reserva1.cancelar()
    except ReservaError as error:
        logging.exception("Operación no permitida sobre la reserva.")
        print("   Error controlado:", error)
    finally:
        print("\nPruebas finalizadas. Revise logs.txt para consultar los eventos y errores.")

    print("\nRESUMEN")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas correctamente: {len(reservas)}")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_pruebas()
