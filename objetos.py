# esta clase unicamente es para pasar los datos de una lista de lista 
# a una lista de objetos.
from Productos import Productos


# ---------- haciendo una lista de objetos ----------
class Objetos:
    def __init__(self, entrada: list):
        self.lista_lista = entrada
        self.lista_de_productos = []


    def asignarValores(self):
        # Iterar a través de las listas internas y crear objetos
        for lista_2 in self.lista_lista:
            codigo, producto, precio_compra, precio_venta, stock = lista_2
            producto_obj = Productos(int(codigo.replace(" ", "")), producto, float(precio_compra.replace(" ", "")), float(precio_venta.replace(" ", "")), int(stock.replace(" ", "")))
            self.lista_de_productos.append(producto_obj)
        return self.lista_de_productos
    


# -------- FUNCIONES -----------
class Funciones:
    def __init__(self, entrada: list):
        self.lista_productos = entrada


    def imprimir(self, cadena: str):
        return cadena

    def imprimirln(self, cadena: str = ""):
        #resultado = (cadena + '\n')
        return cadena

    def conteo(self):
        total_registros = len(self.lista_productos)
        return total_registros

    def promedio(self, clave: str):
        if not self.lista_productos:
            return 0  # Devuelve 0 si la lista está vacía
        
        if not hasattr(self.lista_productos[0], clave):
            return 0  # Devuelve 0 si la clave no existe en los objetos
        
        total_valor = sum(getattr(producto, clave) for producto in self.lista_productos)
        promedio = total_valor / len(self.lista_productos)
        return promedio

    def contarsi(self, clave: str, valor):
        if not self.lista_productos:
            return 0  # Devuelve 0 si la lista está vacía
        
        if not hasattr(self.lista_productos[0], clave):
            return 0  # Devuelve 0 si la clave no existe en los objetos
        
        contador = sum(1 for producto in self.lista_productos if getattr(producto, clave) == valor)
        return contador

    def datos(self):
        if not self.lista_productos:
            return ["No hay registros para mostrar."]
        
        # Obtener los nombres de los atributos de la clase Productos
        atributos = list(vars(self.lista_productos[0]))
        
        # Crear una lista para almacenar los datos
        data = []
        
        # Agregar los títulos de los atributos a la lista de datos
        data.append(atributos)
        
        # Agregar los registros de forma ordenada a la lista de datos
        for producto in self.lista_productos:
            data.append([getattr(producto, atributo) for atributo in atributos])
        
        return data

    def sumar(self, clave: str):
        if not self.lista_productos:
            return 0  # Devuelve 0 si la lista está vacía
        
        if not hasattr(self.lista_productos[0], clave):
            return 0  # Devuelve 0 si la clave no existe en los objetos
        
        total_suma = sum(getattr(producto, clave) for producto in self.lista_productos)
        return total_suma

    def max(self, clave: str):
        if not self.lista_productos:
            return None  # Devuelve None si la lista está vacía
        
        if not hasattr(self.lista_productos[0], clave):
            return None  # Devuelve None si la clave no existe en los objetos

        max_valor = max(getattr(producto, clave) for producto in self.lista_productos)
        return max_valor

    def min(self, clave: str):
        if not self.lista_productos:
            return None  # Devuelve None si la lista está vacía
        
        if not hasattr(self.lista_productos[0], clave):
            return None  # Devuelve None si la clave no existe en los objetos

        min_valor = min(getattr(producto, clave) for producto in self.lista_productos)
        return min_valor

    def exportarReporte(self, titulo, nombre_archivo):
        if not self.lista_productos:
            print("No hay registros para exportar.")
            return
        
        # Abrir el archivo HTML para escritura
        with open(nombre_archivo, 'w') as archivo:
            archivo.write('<!DOCTYPE html>\n<html>\n<head>\n')
            archivo.write(f'<title>{titulo}</title>\n')
            archivo.write('<style>\n')
            archivo.write('table {border-collapse: collapse; width: 100%;}\n')
            archivo.write('th, td {border: 1px solid #dddddd; text-align: left; padding: 8px;}\n')
            archivo.write('tr:nth-child(even) {background-color: #f2f2f2;}\n')
            archivo.write('th {background-color: #4CAF50; color: white;}\n')
            archivo.write('</style>\n')
            archivo.write('</head>\n<body>\n')
            archivo.write(f'<h1>{titulo}</h1>\n')
            archivo.write('<table>\n')

            # Escribir los títulos de los atributos como encabezados de tabla
            atributos = vars(self.lista_productos[0])
            archivo.write('<tr>\n')
            for atributo in atributos:
                archivo.write(f'<th>{atributo}</th>\n')
            archivo.write('</tr>\n')

            # Escribir los registros como filas de la tabla
            for producto in self.lista_productos:
                archivo.write('<tr>\n')
                for atributo in atributos:
                    valor = getattr(producto, atributo)
                    archivo.write(f'<td>{valor}</td>\n')
                archivo.write('</tr>\n')

            archivo.write('</table>\n')
            archivo.write('</body>\n</html>')
            
        print(f'Archivo HTML "{nombre_archivo}" generado exitosamente.')









