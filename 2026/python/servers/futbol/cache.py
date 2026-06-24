
# Cache en archivo para las competiciones (la API tiene rate limit muy bajo)
import json
import os
import time

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
            print('✅ Cache HIT: competiciones')
            return json.load(f)
          
    except FileNotFoundError:
        print('❌ Cache MISS')
        print('El archivo de cache todavía no existe')
        return None

def escribir_cache(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', encoding='utf-8') as f:
        json.dump(datos, f)