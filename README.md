# Software FJ – Sistema Integral de Gestión

## Descripción
Proyecto académico desarrollado en Python para gestionar clientes, servicios y reservas de la empresa ficticia Software FJ. La información se administra mediante objetos y listas en memoria, sin utilizar bases de datos.

## Objetivo
Aplicar programación orientada a objetos y manejo robusto de excepciones para construir una solución modular, estable y extensible.

## Funcionalidades
- Registro de clientes con validación y encapsulación de datos.
- Servicios de reserva de salas, alquiler de equipos y asesorías.
- Cálculo de costos con impuestos y descuentos.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Excepciones personalizadas y registro de eventos y errores en `logs.txt`.
- Diez operaciones demostrativas, con escenarios válidos e inválidos.

## Estructura
- `main.py`: ejecuta las diez operaciones de demostración.
- `entidades.py`: clase abstracta `Entidad` y clase `Cliente`.
- `servicios.py`: clase abstracta `Servicio` y tres servicios especializados.
- `reservas.py`: lógica y estados de las reservas.
- `excepciones.py`: excepciones personalizadas.
- `.gitignore`: excluye archivos temporales y locales.

## Conceptos de programación orientada a objetos
El proyecto utiliza abstracción mediante clases abstractas, herencia en los servicios especializados, encapsulación mediante propiedades, polimorfismo mediante métodos sobrescritos y excepciones personalizadas para controlar errores.

En `servicios.py` se documentan distintas firmas de `calcular_costo` con `typing.overload`. Python no implementa sobrecarga tradicional por firma en tiempo de ejecución; las firmas `@overload` sirven para documentar y apoyar el análisis estático, mientras una única implementación procesa los parámetros opcionales.

## Requisitos
- Python 3.10 o superior.
- No requiere instalar paquetes externos.

## Ejecución
Desde una terminal ubicada en la carpeta del proyecto:

```bash
python main.py
```

En Windows también puede utilizarse:

```bash
py main.py
```

El programa muestra los resultados en la terminal y registra eventos y errores en `logs.txt`.

## Repositorio
https://github.com/lucymenesesnavarro-cmd/Software_FJ
