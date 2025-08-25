from inventario import Inventario
from producto import Producto
from excepciones import ProductoNoEncontradoError

def test_basico():
    inv = Inventario()
    inv.agregar_producto(Producto("A1", "Lápiz", 0.5, 100))
    inv.agregar_producto(Producto("B2", "Cuaderno", 1.5, 50))

    assert inv.obtener_producto("A1").nombre == "Lápiz"
    assert inv.obtener_producto("B2").precio == 1.5

    inv.actualizar_cantidad("A1", 120)
    assert inv.obtener_producto("A1").cantidad == 120

    inv.eliminar_producto("A1")
    try:
        inv.obtener_producto("A1")
        assert False, "Debe lanzar ProductoNoEncontradoError"
    except ProductoNoEncontradoError:
        pass

    print("✅ Todas las pruebas pasaron.")

if __name__ == "__main__":
    test_basico()
