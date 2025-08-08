from artista import Artista


#    Representa una obra del museo, asociada a un artista.
class ObraExtendida:
    def __init__(self, id_obra, titulo, artista: Artista, tipo, fecha_creacion, imagen_url):
    
            self.id_obra = id_obra
            self.titulo = titulo
            self.artista = artista
            self.tipo = tipo
            self.fecha_creacion = fecha_creacion
            self.imagen_url = imagen_url
    

    def mostrar_resumen(self):

        print(f"{self.id_obra} - {self.titulo} ({self.artista.nombre})")

    def mostrar_detalle(self):

        print("----- DETALLE DE OBRA -----")
        print(f"Título: {self.titulo}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creación: {self.fecha_creacion}")
        print(self.artista.descripcion())
        print(f"Imagen: {self.imagen_url}")
