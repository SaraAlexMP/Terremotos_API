######################################################################
### Monjaraz Perez Sara Alexandra ## Instituto Tecnológico de León ###
######################################################################
### API Cliente Terremotos ### Laboratorio Para El Despliegue de   ###
###                        ###    Aplicaciones Empresariales       ###
######################################################################

import requests

# URL base de la API
url_base = "https://earthquake.usgs.gov/fdsnws/event/1/query"

# Función para obtener terremotos en un rango de fechas y con magnitud mínima
def obtener_terremotos(formato, fecha_inicio, fecha_fin, magnitud_minima):
    parametros = {
        "format": formato,                 # Formato de la respuesta
        "starttime": fecha_inicio,         # Fecha de inicio (YYYY-MM-DD)
        "endtime": fecha_fin,              # Fecha de fin (YYYY-MM-DD)
        "minmagnitude": magnitud_minima    # Magnitud mínima
    }
    
    try:
        respuesta = requests.get(url_base, params=parametros)  # Realizar solicitud GET
        if respuesta.status_code == 200:
            return respuesta.json()  # Devolver los datos en formato JSON
        else:
            print(f"Error: Código de estado {respuesta.status_code}")
            return None
    except requests.exceptions.RequestException as error:
        print(f"Error de conexión: {error}")
        return None

# Definir los parámetros de consulta
formato_deseado = "geojson"
fecha_inicio_consulta = "2023-01-01"
fecha_fin_consulta = "2023-01-31"
magnitud_minima = 4.5

# Obtener los datos de terremotos
datos_terremotos = obtener_terremotos(formato_deseado, fecha_inicio_consulta, fecha_fin_consulta, magnitud_minima)

# Procesar y mostrar resultados
if datos_terremotos:
    print(f"Se encontraron {len(datos_terremotos['features'])} terremotos en el periodo indicado:")
    for terremoto in datos_terremotos['features']:
        lugar = terremoto['properties']['place']
        magnitud = terremoto['properties']['mag']
        print(f"Lugar: {lugar}, Magnitud: {magnitud}")
else:
    print("No se encontraron resultados o ocurrió un error.")
