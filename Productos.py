

class Productos:
    def __init__(self, codigo, producto, precio_compra, precio_venta, stock):
        self.codigo = codigo
        self.producto = producto
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock
        
    def imprimir_informacion(self):
        print('-----------------------------')
        print("Código: ", self.codigo)
        print("Producto: ", self.producto)
        print("Precio de Compra: ", self.precio_compra)
        print("Precio de Venta: ", self.precio_venta)
        print("Stock: ", self.stock)
        print('-----------------------------\n')


