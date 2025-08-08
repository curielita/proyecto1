class MetroArt:
    """
    Sistema principal de interacción con el usuario para consultar obras del museo.
    """

    def iniciar(self):
        """
        Muestra el menú principal y gestiona las opciones.
        """
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

    def buscar_y_mostrar_obras(self, url):
        """
        Realiza una búsqueda en la API y muestra las obras de 5 en 5.
        """
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