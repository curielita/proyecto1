from artista import Artista

class ObraExtendida:
    """
    Representa una obra del museo, asociada a un artista.
    """

    def __init__(self, id_obra, titulo, artista: Artista, tipo, fecha_creacion, imagen_url):
        if id_obra != "":
            self.id_obra = id_obra
        else:
            self.id_obra = "N/A"

        if titulo != "":
            self.titulo = titulo
        else:
            self.titulo = "Sin título"

        self.artista = artista

        if tipo != "":
            self.tipo = tipo
        else:
            self.tipo = "Sin tipo"

        if fecha_creacion != "":
            self.fecha_creacion = fecha_creacion
        else:
            self.fecha_creacion = "Desconocida"

        if imagen_url != "":
            self.imagen_url = imagen_url
        else:
            self.imagen_url = "No disponible"

    def mostrar_resumen(self):
        """
        Muestra un resumen breve de la obra.
        """
        print(f"{self.id_obra} - {self.titulo} ({self.artista.nombre})")

    def mostrar_detalle(self):
        """
        Muestra todos los detalles de la obra y su artista.
        """
        print("----- DETALLE DE OBRA -----")
        print(f"Título: {self.titulo}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creación: {self.fecha_creacion}")
        print(self.artista.descripcion())
        print(f"Imagen: {self.imagen_url}")
