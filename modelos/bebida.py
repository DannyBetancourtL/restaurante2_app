from modelos.producto import Producto

# Clase hija que representa una bebida


class Bebida(Producto):

    def __init__(
        self,
        nombre: str,
        precio: float,
        disponible: bool,
        volumen_ml: int,
        tipo_bebida: str
    ):

        super().__init__(nombre, precio, disponible)

        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    # Polimorfismo
    def mostrar_informacion(self) -> None:

        print("========== BEBIDA ==========")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo_bebida}")
        print(f"Volumen: {self.volumen_ml} ml")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Disponible: {self.disponible}")
        print()