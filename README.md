# restaurante2_app
Desarrolle una versión mejorada del sistema restaurante_app utilizando Programación Orientada a Objetos en Python. En esta ocasión, el sistema deberá centrarse en los productos del restaurante, aplicando una relación de herencia entre una clase general y dos clases especializadas.

El proyecto desarrollado por el docente en la Semana 6 corresponde a un sistema de biblioteca donde se aplican clases, objetos, herencia, encapsulación y polimorfismo. En esta tarea, usted deberá tomar ese proyecto únicamente como referencia metodológica para adaptar los mismos principios al contexto de un restaurante. No debe copiar literalmente el código docente, sino analizar su estructura y aplicarla a un problema diferente.

Sistema propuesto: restaurante
El sistema deberá representar productos disponibles en un restaurante. Para ello, se utilizará una clase padre llamada Producto y dos clases hijas: Platillo y Bebida. Esta estructura permitirá evidenciar la herencia, proteger datos internos mediante encapsulación y demostrar polimorfismo al mostrar información diferente según el tipo de producto.

Jerarquía obligatoria:

Producto
├── Platillo
└── Bebida
Entidades mínimas solicitadas:

Producto: clase padre que representa un producto general del restaurante.
Platillo: clase hija que representa una comida o plato del restaurante.
Bebida: clase hija que representa una bebida disponible en el restaurante.
Restaurante: clase de servicio que administra una lista de productos registrados.
 Importante: el estudiante deberá razonar qué atributos corresponden a la clase padre y qué atributos pertenecen únicamente a las clases hijas. La actividad busca que aplique los principios de la POO, no que copie una solución ya desarrollada.
Estructura obligatoria del proyecto
El proyecto deberá organizarse respetando la siguiente estructura de carpetas y archivos:

Estructura mínima:
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py