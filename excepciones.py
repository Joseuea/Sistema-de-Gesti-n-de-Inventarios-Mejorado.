class ErrorInventario(Exception):
    """Excepción base para errores en el inventario."""

class ArchivoCorruptoError(ErrorInventario):
    pass

class PermisoArchivoError(ErrorInventario):
    pass

class ProductoNoEncontradoError(ErrorInventario):
    pass

class ProductoDuplicadoError(ErrorInventario):
    pass
