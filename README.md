# Tienda Ropa POO Bootcamp

## Descripción
Este proyecto implementa un sistema de compra de ropa utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite a los usuarios seleccionar productos de ropa y procesar compras, siguiendo las buenas prácticas de encapsulamiento, herencia, polimorfismo y abstracción.

## Estructura del Proyecto
- **SistemaCompraRopa.py**: Archivo principal que contiene la lógica del programa.
- **README.md**: Documentación del proyecto.

## Clases Implementadas
1. **Producto**: Clase base que representa un producto general.
2. **Ropa**: Clase que hereda de Producto, añadiendo características específicas de la ropa.
3. **Camisa**, **Pantalon**, **Zapato**: Clases derivadas de Ropa que añaden atributos particulares como talla y tipo de tela.
4. **Carrito**: Clase que almacena los productos seleccionados y calcula el total a pagar.
5. **Tienda**: Clase que gestiona los productos disponibles y permite realizar compras.

## Pilares de POO
- **Encapsulamiento**: Los atributos están encapsulados utilizando métodos getters.
- **Herencia**: Ropa hereda de Producto; Camisa y Pantalon heredan de Ropa.
- **Polimorfismo**: El método `mostrar_info` es sobrescrito en cada clase hija para mostrar información específica.
- **Abstracción**: Se ocultan los detalles internos del proceso de compra al usuario.

## Instrucciones para Ejecutar
1. Clona el repositorio.
2. Abre una terminal y navega al directorio del proyecto.
3. Ejecuta el archivo `SistemaCompraRopa.py`:
   ```bash
   python SistemaCompraRopa.py
# Semana-6

