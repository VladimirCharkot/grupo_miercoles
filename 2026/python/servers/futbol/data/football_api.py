import requests
from cache import leer_cache, escribir_cache, cache_equipos, cache_posiciones, cache_equipo, CACHE_COMPETICIONES

API_KEY = "2755c79d8c4e42cf872bc7b3deb965e1"
BASE = "https://api.football-data.org/v4"

def get_tabla_de_posiciones(codigo_de_competicion):
    archivo = cache_posiciones(codigo_de_competicion)
    cache = leer_cache(archivo)
    if cache:
        return cache

    respuesta = requests.get(
        f"{BASE}/competitions/{codigo_de_competicion}/standings",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    datos = respuesta.json()
    escribir_cache(archivo, datos)
    return datos

def get_competiciones():
    cache = leer_cache(CACHE_COMPETICIONES)
    if cache:
        return cache

    respuesta = requests.get(
        f"{BASE}/competitions",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    datos = respuesta.json()
    escribir_cache(CACHE_COMPETICIONES, datos)
    return datos

def get_equipos(codigo_de_competicion):
    archivo = cache_equipos(codigo_de_competicion)
    cache = leer_cache(archivo)
    if cache:
        return cache

    respuesta = requests.get(
        f"{BASE}/competitions/{codigo_de_competicion}/teams",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    datos = respuesta.json()
    escribir_cache(archivo, datos)
    return datos

def get_equipo(id_equipo):
    archivo = cache_equipo(id_equipo)
    cache = leer_cache(archivo)
    if cache:
        return cache

    respuesta = requests.get(
        f"{BASE}/teams/{id_equipo}",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    datos = respuesta.json()
    escribir_cache(archivo, datos)
    return datos
  