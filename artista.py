#Representa a un artista con su información básica.
class Artista:

    def __init__(self, nombre, nacionalidad, nacimiento, fallecimiento):
        if nombre != "":
            self.nombre = nombre
        else:
            self.nombre = "Desconocido"

        if nacionalidad != "":
            self.nacionalidad = nacionalidad
        else:
            self.nacionalidad = "Desconocida"

        if nacimiento != "":
            self.nacimiento = nacimiento
        else:
            self.nacimiento = "N/A"

        if fallecimiento != "":
            self.fallecimiento = fallecimiento
        else:
            self.fallecimiento = "N/A"

    def descripcion(self):
        """
        Devuelve una cadena con la descripción del artista.
        """
        return (
            f"Artista: {self.nombre}\n"
            f"Nacionalidad: {self.nacionalidad}\n"
            f"Año de nacimiento: {self.nacimiento}\n"
            f"Año de fallecimiento: {self.fallecimiento}"
        )