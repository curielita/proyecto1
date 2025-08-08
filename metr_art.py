import requests
import csv
from modelo_obra import ObraExtendida
from artista import Artista
from departamento import Departamento
from nacionalidad import Nacionalidad


#Sistema principal de interacción con el usuario para consultar obras del museo.
class MetroArt:

    #  Muestra el menú principal y gestiona las opciones.
    def iniciar(self):
        while True:
            print("\n===== Sistema MetroArt =====")
            print("1. Consultar obras por Departamento")
            print("2. Consultar obras por Nacionalidad del autor")
            print("3. Consultar obras por Nombre del autor")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.buscar_por_departamento()
            elif opcion == "2":
                self.buscar_por_nacionalidad()
            elif opcion == "3":
                self.buscar_por_autor()
            elif opcion == "4":
                print("Gracias por utilizar MetroArt.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    #Muestra los departamentos y permite buscar obras por uno seleccionado.
    def buscar_por_departamento(self):
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        respuesta = requests.get(url)
        try:
            datos = respuesta.json()
        except:
            print("No se pudo conectar al api.")
            return

        if "departments" not in datos:
            print("No hay departamentos disponibles.")
            return

        departamentos = []
        for item in datos["departments"]:
            depto = Departamento(item["departmentId"], item["displayName"])
            departamentos.append(depto)

        print("\n--- Lista de Departamentos ---")
        for depto in departamentos:
            print(depto)

        depto_id = input("\nIngrese el ID del departamento: ")
        if not depto_id.isdigit():
            print("ID inválido.")
            return

        url_obras = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={depto_id}"
        self.buscar_y_mostrar_obras(url_obras)


    # Permite buscar obras por nacionalidad del autor usando el archivo CSV.
    def buscar_por_nacionalidad(self):
        nacionalidades = []
        try:
            with open("CH_Nationality_List_20171130_v1.csv", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    if fila and fila[0].strip() != "":
                        nacionalidad = Nacionalidad(fila[0])
                        nacionalidades.append(nacionalidad)
        except:
            print("No se cargar nacionalidades.")
            return

        for i, nac in enumerate(nacionalidades):
            print(f"{i + 1}. {nac}")

        seleccion = input("Ingrese el número de la nacionalidad: ")
        if not seleccion.isnumeric():
            print("Valor inválido.")
            return

        index = int(seleccion) - 1
        if index < 0 or index >= len(nacionalidades):
            print("Número fuera de rango.")
            return

        termino = nacionalidades[index].nombre
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={termino}"
        self.buscar_y_mostrar_obras(url)

    #Permite buscar obras por nombre del autor.
    def buscar_por_autor(self):
        autor = input("Ingrese el nombre del autor: ")
        if autor == "":
            print("Nombre vacío.")
            return

        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={autor}"
        self.buscar_y_mostrar_obras(url)

    #Realiza una búsqueda en la API y muestra las obras de 5 en 5.
    def buscar_y_mostrar_obras(self, url):
        respuesta = requests.get(url)
        try:
            datos = respuesta.json()
        except:
            print("No se pudo procesar la respuesta.")
            return

        if "objectIDs" not in datos or not datos["objectIDs"]:
            print("No se encontraron obras.")
            return

        self.mostrar_obras_por_bloque(datos["objectIDs"])

    #Muestra obras en bloques de 5. Permite ver detalles por ID del grupo actual.
    def mostrar_obras_por_bloque(self, lista_ids):
        index = 0
        total = len(lista_ids)

        while index < total:
            grupo_actual = []

            for id_obra in lista_ids[index:index + 5]:
                obra = self.crear_obra_desde_api(id_obra)
                if obra:
                    grupo_actual.append(obra)
                    obra.mostrar_resumen()

            while True:
                opcion = input("\n¿Desea ver detalles de alguna obra? (Si, ingrese numero de ID/ no): ")
                if opcion.lower() == "no":
                    break

                obra_encontrada = None
                for o in grupo_actual:
                    if str(o.id_obra) == opcion:
                        obra_encontrada = o
                        break

                if obra_encontrada:
                    obra_encontrada.mostrar_detalle()
                else:
                    print("No se ecnontro la obra")

            index += 5
            if index < total:
                continuar = input("¿Desea continuar con más obras? (1.para cotinuar / 2. para salir): ")
                if continuar != "1":
                    break

    #Solicita los datos de una obra por ID y devuelve un objeto ObraExtendida.
    def crear_obra_desde_api(self, id_obra):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}"
        respuesta = requests.get(url)
        try:
            datos = respuesta.json()
        except:
            return None

        nombre = datos["artistDisplayName"]
        nacionalidad = datos["artistNationality"]
        nacimiento = datos["artistBeginDate"]
        fallecimiento = datos["artistEndDate"]
        titulo = datos["title"]
        tipo = datos["classification"]
        fecha = datos["objectDate"]
        imagen = datos["primaryImage"] 

        artista = Artista(nombre, nacionalidad, nacimiento, fallecimiento)

        return ObraExtendida(
            id_obra=id_obra,
            titulo= titulo,
            artista=artista,
            tipo=tipo,
            fecha_creacion=fecha,
            imagen_url=imagen
        )
