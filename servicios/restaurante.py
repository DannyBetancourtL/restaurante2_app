from modelos.producto import Producto

# Clase que administra los productos del restaurante


class Restaurante:

    def __init__(self, nombre_restaurante: str):

        self.nombre_restaurante = nombre_restaurante

        # Lista donde se almacenan todos los productos
        self.lista_productos: list[Producto] = []

    # Agregar productos a la lista
    def agregar_producto(self, producto: Producto) -> None:

        self.lista_productos.append(producto)

    # Mostrar todos los productos registrados
    def mostrar_productos(self) -> None:

        print("=" * 55)
        print(f"       RESTAURANTE {self.nombre_restaurante.upper()}")
        print("=" * 55)

        # Demostración del polimorfismo
        for producto in self.lista_productos:
            producto.mostrar_informacion()