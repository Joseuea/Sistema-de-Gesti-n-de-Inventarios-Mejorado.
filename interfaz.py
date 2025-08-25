from inventario import Inventario
from producto import Producto
from excepciones import ProductoDuplicadoError, ProductoNoEncontradoError

def menu():
    print("\n===== Sistema de Inventario =====")
    print("1) Listar productos")
    print("2) Agregar producto")
    print("3) Actualizar cantidad")
    print("4) Actualizar precio")
    print("5) Eliminar producto")
    print("0) Salir")
    return input("Seleccione una opción: ").strip()

def ejecutar_interfaz():
    inv = Inventario()

    while True:
        opcion = menu()
        try:
            if opcion == "1":
                productos = inv.listar_productos()
                if not productos:
                    print("Inventario vacío.")
                else:
                    for p in productos:
                        print(f"{p.id} | {p.nombre} | {p.precio} | {p.cantidad}")
            elif opcion == "2":
                pid = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                inv.agregar_producto(Producto(pid, nombre, precio, cantidad))
                print("✅ Producto agregado.")
            elif opcion == "3":
                pid = input("ID del producto: ").strip()
                cantidad = int(input("Nueva cantidad: "))
                inv.actualizar_cantidad(pid, cantidad)
                print("✅ Cantidad actualizada.")
            elif opcion == "4":
                pid = input("ID del producto: ").strip()
                precio = float(input("Nuevo precio: "))
                inv.actualizar_precio(pid, precio)
                print("✅ Precio actualizado.")
            elif opcion == "5":
                pid = input("ID del producto a eliminar: ").strip()
                inv.eliminar_producto(pid)
                print("✅ Producto eliminado.")
            elif opcion == "0":
                print("Hasta luego.")
                break
            else:
                print("⚠️ Opción inválida.")
        except ProductoDuplicadoError as e:
            print(f"⚠️ {e}")
        except ProductoNoEncontradoError as e:
            print(f"⚠️ {e}")
        except ValueError:
            print("⚠️ Entrada inválida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_interfaz()
