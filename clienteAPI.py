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


