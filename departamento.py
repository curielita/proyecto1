# Representa un departamento del museo.
class Departamento:
    def __init__(self, id_departamento, nombre):
      
        self.id = id_departamento
        self.nombre = nombre


    def __str__(self):
        return f"{self.id} - {self.nombre}"
