from Productos import productos

ruta = '/Users/gio/Desktop/LAB_LFP_2s23/Proyecto2/archivo1.bizdata'


with open(ruta, 'r') as archivo:
    contenido = archivo.read()


'''for linea in contenido:
    linea = linea.rstrip()
    print(linea)'''

class ExitRecursion(Exception):
    pass


class Analizador:
    def __init__(self, entrada:str):
        self.lineas = entrada #ENTRADA
        self.index = 0 #POSICION DE CARACTERES EN LA ENTRADA
        self.fila = 1 #FILA ACTUAL
        self.columna = 1 #COLUMNA ACTUAL
        self.claves = [] #El nombre de las claves
        self.lista_resgistros = [] # Lista con listas de los valores de Registro

        self.ListaErroresS = [] # LISTA PARA GUARDAR ERRORES
        self.ListaErroresL = []
        
    
    def _token(self, token: str, estado_actual: str, estado_sig: str):
    # Ignorar espacios en blanco y saltos de línea mientras avanzamos en el texto
        while self.index < len(self.lineas) and (self.lineas[self.index] == " " or self.lineas[self.index] == "\n"):
            if self.lineas[self.index] == " ":
                # Incrementar la columna si encontramos un espacio en blanco
                self.columna += 1
            elif self.lineas[self.index] == "\n":
                # Si encontramos un salto de línea, reiniciar la columna y aumentar la línea
                self.columna = 1
                self.fila += 1
            # Avanzar al siguiente carácter en el texto
            self.index += 1

        if self.index < len(self.lineas):
            # Si aún no hemos alcanzado el final del texto, juntar el token
            text = self._juntar(self.index, len(token))
            # Luego, analizar el token
            if self._analizar(token, text):
                self.index += len(token) - 1
                self.columna += len(token) - 1
                return estado_sig
            else:
                return 'ERROR'
        else:
            return estado_actual

    def _juntar(self,_index:int, _count:int):
        try:
            tmp = ''
            for i in range(_index, _index + _count):
                tmp += self.lineas[i]
            return tmp
        except:
            return None
        
    def _analizar(self, token, texto):
        try:
            count = 0
            tokem_tmp = ""
            for i in texto:
                #CUANDO LA LETRA HAGA MATCH CON EL TOKEN ENTRA
                print('COMBINACION -> ',i , '==', token[count])
                if str(i) == str(token[count]):
                    tokem_tmp += i  
                    count += 1 
                else:
                    #print('ERROR1')
                    return False
                
            print(f'\nENCONTRE --> {tokem_tmp} <--\n')
            return True
        except:
            #print('ERROR2')
            return False

    def analizarCadena():
        pass

    def _compile(self):
        estado_actual = 'S0'
        #mientras no sea vacio se sale
        while self.lineas[self.index] != "":
            print(f'CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 0
            else:
                self.columna +=1

            # ************************
            #         ESTADOS
            # ************************

            #S0 -> Claves S1
            if estado_actual == 'S0':
                comentarioSimple = self._token('#', 'S0', 'Comentario')
                if comentarioSimple == "Comentario":
                    print('Aqui va un comentario')
                    self._comentarioSimple()
                else:
                    estado_actual = self._token('Claves', 'S0', 'S1')
            # S1 -> = S2   
            elif estado_actual == 'S1':
                estado_actual = self._token('=', 'S1', 'S2')

            # S2 -> [ S3
            elif estado_actual == 'S2':
                estado_actual = self._token('[', 'S2', 'S3')

            #S3 -> " S8
            elif estado_actual == 'S3':
                try:
                    estado_actual = self._claves(estado_actual)
                except ExitRecursion:
                    self.index = self.index - 1
                    estado_actual = 'S8'

            #S8 -> ] S9
            elif estado_actual == 'S8':
                estado_actual= self._token(']', 'S8', 'S9')

            #S9 -> Registros S10
            elif estado_actual == 'S9':
                comentarioSimple = self._token('#', 'S9', 'Comentario')
                if comentarioSimple == "Comentario":
                    print('Aqui va un comentario')
                    self._comentarioSimple()
                else:
                    estado_actual= self._token('Registros', 'S9', 'S10')

            #S10 -> = S11
            elif estado_actual == 'S10':
                estado_actual= self._token('=', 'S10', 'S11')

            #S11 ->[ S12
            elif estado_actual == 'S11':
                estado_actual= self._token('[', 'S11', 'S12')

            #S12 -> { S13
            elif estado_actual == 'S12':
                try:
                    #recursivo para los registros (S12)
                    estado_actual = self._registros(estado_actual)
                except ExitRecursion:
                    self.index = self.index - 1
                    estado_actual = 'S23'

            #S13 -> ] S14
            elif estado_actual == 'S23':
                estado_actual= self._token(']', 'S23', 'S24')

            #S24 -> funciones S25
            elif estado_actual == 'S24':
                print('AQUI VAN LAS FUNCIONES')
                self._funciones(estado_actual)

            # ERRORES 
            if estado_actual == 'ERROR':
                print('---> AQUI OCURRIO UN ERROR\n')
                estado_actual = 'S0'

            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _comentarioSimple(self):
        estado_actual = 'S0'
        #mientras no sea vacio se sale
        while self.lineas[self.index+1] != "":
            print(f'CC) CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            if self.lineas[self.index] == '\n':
                return

            # IDENTIFICAR SALTO DE LINEA
            elif self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 0
            else:
                self.columna +=1

            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _claves(self, estadoActual):
        #S3
        estado_actual = estadoActual
        #mientras no sea vacio se sale
        while self.lineas[self.index] != "":
            print(f'claves) CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 1

            elif self.lineas[self.index] == ']':
                #S7 -> ] S8
                raise ExitRecursion
            else:
                self.columna +=1

            # S3 -> " S4 (comillas de inico)
            if estado_actual == 'S3':
                estado_actual = self._token('"', 'S3', 'S4')

            # S4 -> clave_1 S5
            elif estado_actual == 'S4':
                estado_sig = self._info(estado_actual, self.claves)
                print(self.claves)
                #S5 -> " S6 (comillas de cierre)
                estado_actual = self._token('"', estado_sig, 'S6')

            elif estado_actual == 'S6':
                estado_actual = self._token(',', 'S6', 'S7')
            
            #aqui se vuelve recursivo
            # S7 -> " S3 (comillas de inico)
            elif estado_actual == 'S7':
                estado_sig = 'S3'
                self._claves(estado_sig)

            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _info(self, estadoActual, claves):
        estado_actual = estadoActual
        palabra = ""  # Inicializa una cadena vacía para almacenar la palabra leída

        while self.index < len(self.lineas):
            print(f'infoC) CARACTER - {self.lineas[self.index]} | ESTADO - {estado_actual} | FILA - {self.fila} | COLUMNA - {self.columna}')

            if self.lineas[self.index] == '"':
                if palabra:
                    claves.append(palabra)  # Agrega la palabra a la lista "claves" si no está vacía
                return 'S5'

            # IDENTIFICAR SALTO DE LINEA
            elif self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 0
            else:
                palabra += self.lineas[self.index]  # Agrega el carácter a la palabra

            self.columna += 1

            # INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index += 1
            else:
                break

        if palabra:
            claves.append(palabra)  # Agrega la última palabra a la lista "claves" si no está vacía

    def _registros(self, estadoActual):
        lista_temp =[]
        #S12
        estado_actual = estadoActual

        #mientras no sea vacio se sale
        while self.lineas[self.index] != "":
            print(f'Registro) CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 1

            elif self.lineas[self.index] == ']':
                #S12 -> ] S13
                raise ExitRecursion
            else:
                self.columna +=1

            # S12 -> { S13 (llave de inico)
            if estado_actual == 'S12':
                estado_actual = self._token('{', 'S12', 'S13')

            #aqui debo guardar los valores
            # S13 -> valores S14
            elif estado_actual == 'S13':
                estado_sig = self._infoRegistros(estado_actual, lista_temp)
                #retornar S14
                print(lista_temp)
                # S14 -> , S15 
                estado_actual = self._token(',', estado_sig, 'S13')
                if estado_actual == "ERROR":
                    estado_actual = 'S15'
                    self.index = self.index - 1

            #si viene una } es posible que vengan más registros
            # S15 -> } S16
            elif estado_actual == 'S15':
                estado_actual = self._token('}', 'S15', 'S16')

            # Aqui se vuelve recursivo
            # S16 -> { S12 (llaves de inico)
            elif estado_actual == 'S16':
                estado_sig = 'S12'
                self.index = self.index + 1
                self.lista_resgistros.append(lista_temp)
                self._registros(estado_sig)

            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break   

    def _infoRegistros(self, estadoActual, valores):
        estado_actual = estadoActual
        palabra = ""  # Inicializa una cadena vacía para almacenar la palabra leída

        while self.index < len(self.lineas):
            print(f'infoR) CARACTER - {self.lineas[self.index]} | ESTADO - {estado_actual} | FILA - {self.fila} | COLUMNA - {self.columna}')

            if self.lineas[self.index] == ',' or self.lineas[self.index] == '}':
                if palabra:
                    valores.append(palabra)  # Agrega la palabra a la lista "valores" si no está vacía
                return 'S14'

            # IDENTIFICAR SALTO DE LINEA
            elif self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 0
            else:
                palabra += self.lineas[self.index]  # Agrega el carácter a la palabra

            self.columna += 1

            # INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index += 1
            else:
                break

        if palabra:
            valores.append(palabra)  # Agrega la última palabra a la lista "valores" si no está vacía

    # Debe ser recursivo para hallar todas las funciones posibles 
    def _funciones(self, estadoActual):
            #S3
        estado_actual = estadoActual
        #mientras no sea vacio se sale
        while self.lineas[self.index] != "":
            print(f'claves) CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 1

            elif self.lineas[self.index] == ']':
                #S7 -> ] S8
                raise ExitRecursion
            else:
                self.columna +=1

            # S3 -> " S4 (comillas de inico)
            if estado_actual == 'S3':
                estado_actual = self._token('"', 'S3', 'S4')

            # S4 -> clave_1 S5
            elif estado_actual == 'S4':
                estado_sig = self._info(estado_actual, self.claves)
                print(self.claves)
                #S5 -> " S6 (comillas de cierre)
                estado_actual = self._token('"', estado_sig, 'S6')

            elif estado_actual == 'S6':
                estado_actual = self._token(',', 'S6', 'S7')
            
            #aqui se vuelve recursivo
            # S7 -> " S3 (comillas de inico)
            elif estado_actual == 'S7':
                estado_sig = 'S3'
                self._claves(estado_sig)

            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _comentarioMulti(self):
            estado_actual = 'S0'
            
            #mientras no sea vacio se sale
            while self.lineas[self.index] != "":
                
                print(f'MULTI - CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
                
                # IDENTIFICAR SALTO DE LINEA
                if self.lineas[self.index] == "'":
                    self.index = self.index + 1
                    if self.lineas[self.index] == "'":
                        self.index = self.index + 1
                        if self.lineas[self.index] == "'":
                            return 'comentario'

                # IDENTIFICAR SALTO DE LINEA
                elif self.lineas[self.index] == '\n':
                    self.fila += 1
                    self.columna = 0
                else:
                    self.columna +=1

                #INCREMENTAR POSICION
                if self.index < len(self.lineas) - 1:
                    self.index +=1
                else:
                    break

    def guardarErrores(self, token, fila, columna):
        self.ListaErrores.append({"token":token, "fila": fila, "columna":columna})




a = Analizador(contenido)
a._compile()

print('\nTitulos ',a.claves)
for i in a.claves:
    i = i.replace(" ", "")
    print(i)


print('\n',a.lista_resgistros,'\n')
for i in a.lista_resgistros:
    print(i)

print('conteo() ', len(a.lista_resgistros))


for i in a.lista_resgistros:
    print('------------')
    count = 1
    for j in i:
        j = j.replace(" ", "")
        print(f"{count}) ",j)
        count = count + 1
    print('------------')
    print('\n')

# Crear una lista para almacenar objetos de la clase Productos
lista_de_productos = []

# Iterar a través de las listas internas y crear objetos
for lista_2 in a.lista_resgistros:
    codigo, producto, precio_compra, precio_venta, stock = lista_2
    producto_obj = productos(codigo, producto, precio_compra, precio_venta, stock)
    lista_de_productos.append(producto_obj)

# Ahora, lista_de_productos contiene objetos de la clase Productos con los valores de lista_2
# Puedes acceder a los atributos de los objetos de la siguiente manera:
for producto_obj in lista_de_productos:
    print('-----------------------------')
    print(f"Código: {(producto_obj.codigo)}")
    print(f"Producto: {producto_obj.producto}")
    print(f"Precio de Compra: {(producto_obj.precio_compra)}")
    print(f"Precio de Venta: {producto_obj.precio_venta}")
    print(f"Stock: {producto_obj.stock}")
    print('-----------------------------\n')