from modelos.producto import Producto

class Inventario:

    def __init__(self):
        self.productos = []  # lista principal

    def agregar(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            raise ValueError("ID repetido.")
        self.productos.append(producto)

    def eliminar(self, id_prod):
        self.productos = [p for p in self.productos if p.get_id() != id_prod]

    def actualizar(self, id_prod, nueva_cant=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_prod:
                if nueva_cant is not None:
                    p.set_cantidad(nueva_cant)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return
        raise ValueError("Producto no encontrado.")

    def buscar(self, nombre):
        nombre = nombre.lower()
        return [p for p in self.productos if nombre in p.get_nombre().lower()]

    def listar(self):
        return self.productos