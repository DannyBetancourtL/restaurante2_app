from modelos.producto import Producto

# Clase hija que representa un platillo


class Platillo(Producto):

    def __init__(
        self,
        nombre: str,
        precio: float,
        disponible: bool,
        tipo_platillo: str,
        tiempo_preparacion: int
    ):

        super().__init__(nombre, precio, disponible)

        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion

    # Polimorfismo
    def mostrar_informacion(self) -> None:

        print("========== PLATILLO ==========")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo_platillo}")
        print(f"Tiempo de preparación: {self.tiempo_preparacion} minutos")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Disponible: {self.disponible}")
        print()