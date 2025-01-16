# ScribeLog

[Read this in English](README.md) | [Leer esto en español](README_es.md)

ScribeLog es una biblioteca ligera de Python para registrar mensajes en archivos de texto. Ofrece validación de rutas y soporte opcional para marcas de tiempo en las entradas de registro.

## Características

- Registrar mensajes en un archivo `.log` especificado.
- Validar la ruta y la extensión del archivo.
- Agregar marcas de tiempo a las entradas del registro.
- Configuración y uso simples.

## Instalación

Para instalar ScribeLog, ejecuta:
```bash
pip install ScribeLog
```

## Uso

```python
from ScribeLog import ConfigLog, Log, GetPathLogin

# Configurar el archivo de registro
ConfigLog("/ruta/a/tuarchivo.log")

# Registrar un mensaje con marca de tiempo
Log("Este es un mensaje de prueba.")

# Registrar un mensaje sin marca de tiempo
Log("Otro mensaje de prueba.", time=False)

# Recuperar la ruta actual del archivo de registro
print(GetPathLogin())
```

## Licencia

ScribeLog está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
