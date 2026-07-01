
# Cache en archivo para las competiciones (la API tiene rate limit muy bajo)
import json
import os
import time
from functools import wraps

CACHE_COMPETICIONES = 'data/cache_competiciones.json'

# Para los equipos la cache depende de la competición, así que el id_codigo
# forma parte del nombre del archivo (una cache por competición).
def cache_equipos(id_competicion):
    return f'data/cache_equipos_{id_competicion}.json'

# La tabla de posiciones también depende de la competición.
def cache_posiciones(id_competicion):
    return f'data/cache_posiciones_{id_competicion}.json'

# Y la info de un equipo depende de su id.
def cache_equipo(id_equipo):
    return f'data/cache_equipo_{id_equipo}.json'

# Tiempo de vida de la cache en segundos (por defecto 24 horas)
TTL_CACHE = 60 * 60 * 24

# Time to live
def leer_cache(nombre_archivo, ttl=TTL_CACHE):
    try:
      
        # Si el archivo es más viejo que el TTL, lo tratamos como inexistente
        antiguedad = time.time() - os.path.getmtime(nombre_archivo)
        if antiguedad > ttl:
            print('⌛ Cache vencida')
            return None
        with open(nombre_archivo, encoding='utf-8') as f:
            print(f'✅ Cache HIT: {nombre_archivo}')
            return json.load(f)
          
    except FileNotFoundError:
        print('❌ Cache MISS')
        print('El archivo de cache todavía no existe')
        return None

def escribir_cache(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', encoding='utf-8') as f:
        json.dump(datos, f)


# Decorador que le agrega cache en archivo a cualquier función.
#
# El parámetro `nombre_archivo` es VARIABLE: puede ser
#   - un string fijo            -> ej: CACHE_COMPETICIONES
#   - una función que calcula    -> ej: cache_posiciones(codigo)
#     el path a partir de los mismos argumentos que recibe la función cacheada.
#
# Así, get_tabla_de_posiciones('PD') usa 'data/cache_posiciones_PD.json'
# y get_tabla_de_posiciones('CL') usa 'data/cache_posiciones_CL.json'.
def con_cache(nombre_archivo):
    def decorador(fn):
        @wraps(fn)
        def envuelto(*args, **kwargs):
            # Si nos pasaron una función, la usamos para armar el path con los argumentos.
            archivo = nombre_archivo(*args, **kwargs) if callable(nombre_archivo) else nombre_archivo

            cache = leer_cache(archivo)
            if cache is not None:
                return cache

            datos = fn(*args, **kwargs)
            escribir_cache(archivo, datos)
            return datos
        return envuelto
    return decorador