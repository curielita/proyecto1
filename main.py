from services.api_service import obtener_departamentos, buscar_obras_por_departamento, obtener_detalles_obra
from services.image_service import guardar_imagen_desde_url, mostrar_imagen

def mostrar_menu():
    print("\n=== METROART ===")
    print("1. Ver obras por departamento")
    print("2. Ver detalles de una obra")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            departamentos = obtener_departamentos()
            for dep in departamentos:
                print(f"{dep['departmentId']}: {dep['displayName']}")
            dep_id = input("Ingrese el ID del departamento: ")
            ids = buscar_obras_por_departamento(dep_id)
            for oid in ids:
                obra = obtener_detalles_obra(oid)
                print(f"{obra.object_id} - {obra.title} - {obra.artist.name}")
        
        elif opcion == "2":
            object_id = input("Ingrese el ID de la obra: ")
            obra = obtener_detalles_obra(object_id)
            print(f"\nTítulo: {obra.title}")
            print(f"Artista: {obra.artist.name}")
            print(f"Nacionalidad: {obra.artist.nationality}")
            print(f"Nacimiento: {obra.artist.birth_year}")
            print(f"Fallecimiento: {obra.artist.death_year}")
            print(f"Tipo: {obra.classification}")
            print(f"Año: {obra.object_date}")
            print(f"Imagen: {obra.image_url}")

            if obra.image_url:
                archivo = guardar_imagen_desde_url(obra.image_url, f"obra_{obra.object_id}")
                mostrar_imagen(archivo)

        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
