# Software FJ – Sistema Integral de Gestión

Proyecto académico en Python para gestionar clientes, servicios y reservas sin utilizar bases de datos.

## Archivos
- `main.py`: ejecución y demostración de 10 operaciones.
- `entidades.py`: clase abstracta Entidad y clase Cliente.
- `servicios.py`: clase abstracta Servicio y tres servicios especializados.
- `reservas.py`: creación, confirmación, cancelación y procesamiento de reservas.
- `excepciones.py`: excepciones personalizadas.
- `logs.txt`: se genera automáticamente al ejecutar el programa.

## Requisitos
Python 3.10 o superior. No requiere instalar librerías externas.

## Ejecución
Desde la terminal de Visual Studio Code, dentro de esta carpeta, ejecutar:

```bash
python main.py
```

En algunos equipos Windows puede ser necesario usar:

```bash
py main.py
```

El programa muestra los resultados en la terminal y crea/actualiza `logs.txt` con eventos y errores.
