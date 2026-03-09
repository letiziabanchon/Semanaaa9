from servicios.inventario import Inventario
from modelos.producto import Producto

inv = Inventario()

def menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("99. Salir")

while True:
    menu()
    op = input("Opción: ")

    if op == "99":
        break

    elif op == "1":
        idp = input("ID: ")
        nom = input("Nombre: ")
        cant = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inv.agregar(Producto(idp, nom, cant, precio))
        print("Producto agregado.")

    elif op == "2":
        idp = input("ID a eliminar: ")
        inv.eliminar(idp)
        print("Producto eliminado.")

    elif op == "3":
        idp = input("ID: ")
        cant = input("Nueva cantidad (Enter para omitir): ")
        precio = input("Nuevo precio (Enter para omitir): ")

        cant = int(cant) if cant else None
        precio = float(precio) if precio else None
        
        inv.actualizar(idp, cant, precio)
        print("Producto actualizado.")

    elif op == "4":
        nom = input("Nombre a buscar: ")
        res = inv.buscar(nom)
        for p in res:
            print(p)

    elif op == "5":
        for p in inv.listar():
            print(p)