class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo privado
        self._precio = precio  # Atributo privado

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio:.2f}")


class Ropa(Producto):
    def __init__(self, nombre, precio, tipo_tela):
        super().__init__(nombre, precio)
        self._tipo_tela = tipo_tela  # Atributo privado

    @property
    def tipo_tela(self):
        return self._tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de tela: {self.tipo_tela}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, tipo_tela, talla):
        super().__init__(nombre, precio, tipo_tela)
        self._talla = talla  # Atributo privado

    @property
    def talla(self):
        return self._talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, tipo_tela, talla):
        super().__init__(nombre, precio, tipo_tela)
        self._talla = talla  # Atributo privado

    @property
    def talla(self):
        return self._talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, tipo_tela, talla):
        super().__init__(nombre, precio, tipo_tela)
        self._talla = talla  # Atributo privado

    @property
    def talla(self):
        return self._talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class Carrito:
    def __init__(self):
        self.productos = []  # Lista para almacenar los productos

    def agregar_producto(self, producto):
        self.productos.append(producto)  # Agrega un producto al carrito

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)  # Suma los precios
        return total

    def mostrar_resumen(self):
        print("\nResumen de la compra:")
        for producto in self.productos:
            producto.mostrar_info()
        print(f"Total a pagar: ${self.calcular_total():.2f}")


class Tienda:
    def __init__(self):
        self.productos = []  # Lista de productos disponibles

    def agregar_producto(self, producto):
        self.productos.append(producto)  # Agrega un producto a la tienda

    def mostrar_productos(self):
        print("Productos disponibles:")
        for idx, producto in enumerate(self.productos, start=1):
            print(f"{idx}. {producto.nombre} - ${producto.precio:.2f}")

    def comprar(self):
        carrito = Carrito()
        while True:
            self.mostrar_productos()
            seleccion = input("Seleccione el número del producto a comprar (o 'salir' para finalizar): ")
            if seleccion.lower() == 'salir':
                break
            try:
                index = int(seleccion) - 1
                if 0 <= index < len(self.productos):
                    cantidad = int(input("Ingrese la cantidad: "))
                    for _ in range(cantidad):
                        carrito.agregar_producto(self.productos[index])
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        carrito.mostrar_resumen()


if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_producto(Camisa("Camisa Casual", 29.99, "Algodón", "M"))
    tienda.agregar_producto(Pantalon("Pantalón de Mezclilla", 49.99, "Denim", "L"))
    tienda.agregar_producto(Zapato("Zapatos de Cuero", 79.99, "Cuero", "42"))
    
    tienda.comprar()
