import requests

API_KEY = "2755c79d8c4e42cf872bc7b3deb965e1"
BASE = "https://api.football-data.org/v4"

def get_tabla_de_posiciones(codigo_de_competicion):
    respuesta = requests.get(
        f"{BASE}/competitions/{codigo_de_competicion}/standings",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    return respuesta.json()

def get_competiciones():
    respuesta = requests.get(
        f"{BASE}/competitions",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    return respuesta.json()

def get_equipos(codigo_de_competicion):
    respuesta = requests.get(
        f"{BASE}/competitions/{codigo_de_competicion}/teams",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    return respuesta.json()

def get_equipo(id_equipo):
    respuesta = requests.get(
        f"{BASE}/teams/{id_equipo}",
        headers={"X-Auth-Token": API_KEY}
    )
    respuesta.raise_for_status()
    return respuesta.json()
  