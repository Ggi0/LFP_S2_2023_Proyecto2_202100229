
ruta = '/Users/gio/Desktop/LAB_LFP_2s23/Proyecto2/archivo1.bizdata'
with open(ruta, 'r') as archivo:
    contenido = archivo.read()

class productos:
    def __init__(self, codigo, producto, precio_compra, precio_venta, stock):
        self.codigo = codigo
        self.producto = producto
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock

    def asignarValores(self):
        pass
        


