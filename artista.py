#Representa a un artista con su información básica.
class Artista:

    def __init__(self, nombre, nacionalidad, nacimiento, fallecimiento):
            self.nombre = nombre
            self.nacionalidad = nacionalidad
            self.nacimiento = nacimiento
            self.fallecimiento = fallecimiento
    def descripcion(self):
        return (
            f"Artista: {self.nombre}\n"
            f"Nacionalidad: {self.nacionalidad}\n"
            f"Año de nacimiento: {self.nacimiento}\n"
            f"Año de fallecimiento: {self.fallecimiento}"
        )