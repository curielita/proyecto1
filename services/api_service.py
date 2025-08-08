import requests
from models.artwork import Artwork, Artist

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def obtener_departamentos():
    """Devuelve una lista de departamentos del museo."""
    response = requests.get(f"{BASE_URL}/departments")
    response.raise_for_status()
    return response.json()["departments"]

def buscar_obras_por_departamento(department_id):
    """Devuelve una lista de IDs de obras en un departamento."""
    response = requests.get(f"{BASE_URL}/objects?departmentIds={department_id}")
    response.raise_for_status()
    return response.json()["objectIDs"][:20]  # Limitamos para hacer pruebas

def obtener_detalles_obra(object_id):
    """Obtiene los datos de una obra específica."""
    response = requests.get(f"{BASE_URL}/objects/{object_id}")
    response.raise_for_status()
    data = response.json()

    artist = Artist(
        data.get("artistDisplayName", "Desconocido"),
        data.get("artistNationality", "Desconocida"),
        data.get("artistBeginDate", "N/D"),
        data.get("artistEndDate", "N/D"),
    )

    artwork = Artwork(
        object_id,
        data.get("title", "Sin título"),
        artist,
        data.get("classification", "Sin clasificar"),
        data.get("objectDate", "Desconocida"),
        data.get("primaryImage", ""),
    )
    return artwork
