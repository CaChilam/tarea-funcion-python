# 1. Creación de la colección (diccionario)
inventario = {
    "manzana": 0.50,
    "leche": 1.20
}

def gestionar_tienda():
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar/Actualizar producto")
        print("2. Mostrar inventario")
        print("3. Buscar precio de un producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        # 2. Funcionalidad para insertar/agregar datos
        if opcion == "1":
            nombre = input("Nombre del producto: ").lower()
            precio = float(input("Precio: "))
            inventario[nombre] = precio
            print(f"Producto{nombre} guardado.")

            # 3. Mostrar la informacón almacenada
        elif opcion == "2":
            print("\nLista de productos:")
            for producto, precio in inventario.items():
                print(f"- {producto}: ${precio}")

                # 4. Operación adicional: Buscar
        elif opcion == "3":
            nombre = input("¿Qué producto buscas?: ").lower()
            if nombre in inventario:
                print(f"El precio de {nombre} es ${inventario[nombre]}")
            else:
                print("Producto no encontrado.")

                # 4. Operación adicional: Eliminar
        elif opcion == "4":
            nombre = input("nombre del producto a eliminar: ").lower()
            if nombre in inventario:
                del inventario[nombre]
                print(f"{nombre} eliminado.")
            else:
                print("No existe ese producto.")

        elif opcion == "5":
            break

if __name__== "__main__":
    gestionar_tienda()
