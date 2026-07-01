import requests
from cache import con_cache, cache_equipos, cache_posiciones, cache_equipo, CACHE_COMPETICIONES

API_KEY = "2755c79d8c4e42cf872bc7b3deb965e1"
BASE = "https://api.football-data.org/v4"


# Helper: hace el pedido a la API y devuelve el JSON (o lanza error si falló).
def _pedir(ruta):
    respuesta = requests.get(f"{BASE}{ruta}", headers={"X-Auth-Token": API_KEY})
    respuesta.raise_for_status()
    return respuesta.json()


@con_cache(CACHE_COMPETICIONES)
def get_competiciones():
    """Pide la lista de competiciones a football-data"""
    return _pedir("/competitions")


@con_cache(cache_posiciones)
def get_tabla_de_posiciones(codigo_de_competicion):
    return _pedir(f"/competitions/{codigo_de_competicion}/standings")


@con_cache(cache_equipos)
def get_equipos(codigo_de_competicion):
    return _pedir(f"/competitions/{codigo_de_competicion}/teams")


@con_cache(cache_equipo)
def get_equipo(id_equipo):
    return _pedir(f"/teams/{id_equipo}")
