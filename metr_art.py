class MetroArt:
    """
    Sistema principal de interacción con el usuario para consultar obras del museo.
    """
#Muestra el menú principal y gestiona las opciones.
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

    def buscar_por_departamento(self):
        """
        Muestra los departamentos y permite buscar obras por uno seleccionado.
        """
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        respuesta = requests.get(url)
        try:
            datos = respuesta.json()
        except:
            print("No se pudo conectar con el servidor.")
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
                        nacionalidad = Nacionalidad(fila[0].strip())
                        nacionalidades.append(nacionalidad)
        except:
            print("No se pudo leer el archivo de nacionalidades.")
            return

        for i, nac in enumerate(nacionalidades):
            print(f"{i + 1}. {nac}")

        seleccion = input("Ingrese el número de la nacionalidad: ")
        if not seleccion.isdigit():
            print("Valor inválido.")
            return

        index = int(seleccion) - 1
        if index < 0 or index >= len(nacionalidades):
            print("Número fuera de rango.")
            return

        termino = nacionalidades[index].nombre
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={termino}"
        self.buscar_y_mostrar_obras(url)

    def mostrar_obras_por_bloque(self, lista_ids):
        """
        Muestra obras en bloques de 5. Permite ver detalles por ID del grupo actual.
        """
        index = 0
        total = len(lista_ids)

        while index < total:
            print(f"\n--- Mostrando obras {index + 1} a {min(index + 5, total)} de {total} ---\n")
            grupo_actual = []

            for id_obra in lista_ids[index:index + 5]:
                obra = self.crear_obra_desde_api(id_obra)
                if obra:
                    grupo_actual.append(obra)
                    obra.mostrar_resumen()

            while True:
                opcion = input("\n¿Desea ver detalles de alguna obra? (ID / no): ")
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
                    print("ID no encontrado en este grupo.")

            index += 5
            if index < total:
                continuar = input("¿Desea continuar con más obras? (s/n): ")
                if continuar.lower() != "s":
                    break


    def crear_obra_desde_api(self, id_obra):
        """
        Solicita los datos de una obra por ID y devuelve un objeto ObraExtendida.
        """
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
