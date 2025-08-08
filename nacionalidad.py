#Representa una nacionalidad disponible para buscar autores.
class Nacionalidad:
    def __init__(self, nombre):
        if nombre != "":
            self.nombre = nombre
        else:
            self.nombre = "Desconocida"

    def __str__(self):
        return self.nombre
