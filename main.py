from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

# ==========================
# Crear el restaurante
# ==========================
restaurante_lojano = Restaurante("Sabor Lojano")

# Crear platillos típicos
platillo_1 = Platillo( "Cecina Lojana", 5.50, True, "Plato fuerte", 25)
platillo_2 = Platillo( "Repe Lojano", 3.75, True, "Sopa", 15)

# Crear bebidas
bebida_1 = Bebida( "Horchata Lojana", 1.00, True, 400,"Natural de hierbas")
bebida_2 = Bebida("Jugo de Tomate", 1.50, True, 500, "Natural")

# Agregar productos
restaurante_lojano.agregar_producto(platillo_1)
restaurante_lojano.agregar_producto(platillo_2)
restaurante_lojano.agregar_producto(bebida_1)
restaurante_lojano.agregar_producto(bebida_2)

# ==========================
# Menú principal
# ==========================

while True:

    print("\n")
    print("=" * 50)
    print("     RESTAURANTE SABOR LOJANO")
    print("=" * 50)
    print("1. Ver menú")
    print("2. Tomar una orden")
    print("3. Salir")
    print("=" * 50)

    opcion = input("Seleccione una opción: ")

    # Mostrar menú
    if opcion == "1":

        print("\nMENÚ DISPONIBLE\n")

        for indice, producto in enumerate(restaurante_lojano.lista_productos, start=1):
            print(f"{indice}. {producto.nombre} - ${producto.obtener_precio():.2f}")

    # Tomar pedido
    elif opcion == "2":

        pedido = []
        total = 0

        while True:

            print("\nSeleccione un producto:\n")

            for indice, producto in enumerate(restaurante_lojano.lista_productos, start=1):
                print(f"{indice}. {producto.nombre} - ${producto.obtener_precio():.2f}")

            seleccion = int(input("\nNúmero del producto: "))

            if 1 <= seleccion <= len(restaurante_lojano.lista_productos):

                producto = restaurante_lojano.lista_productos[seleccion - 1]

                pedido.append(producto)

                total += producto.obtener_precio()

                continuar = input("¿Desea agregar otro producto? (S/N): ")

                if continuar.lower() != "s":
                    break

            else:
                print("Producto no válido.")

        # Mostrar factura
        print("\n")
        print("=" * 45)
        print("         FACTURA")
        print("=" * 45)

        for producto in pedido:
            print(f"{producto.nombre:<25} ${producto.obtener_precio():>6.2f}")

        print("-" * 45)
        print(f"TOTAL A PAGAR:          ${total:.2f}")
        print("=" * 45)

    elif opcion == "3":

        print("\nGracias por visitar Sabor Lojano.")
        break

    else:
        print("Opción incorrecta.")
