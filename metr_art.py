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