
from objetos import Objetos
from objetos import Funciones
'''
#ruta = '/Users/gio/Desktop/LAB_LFP_2s23/Proyecto2/LFP_S2_2023_Proyecto2_202100229/archivo1.bizdata'
ruta = '/Users/gio/Desktop/LAB_LFP_2s23/Proyecto2/LFP_S2_2023_Proyecto2_202100229/prueba.bizdata'

with open(ruta, 'r') as archivo:
    contenido = archivo.read()'''


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
        self.lista_resgistros = [] # Lista con listas de los valores de Registro -> que seran objetos Productos

        self.lista_resultados = [] #lista en donde guardo los resultados

        self.lista_token = [] #lista para guadar los token 

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
            # Luego, analizar el token
            if self._analizar(token, text):
                # Asegurarse de que solo devolvemos estado_sig si hemos encontrado una coincidencia completa con el token.
                # Aquí es donde se ha realizado el cambio. Ahora comprobamos que el texto coincide completamente con el token antes de devolver estado_sig.
                if (text) == (token):

                    tokenD = token
                    lineaD = self.fila
                    columnaD = self.columna

                    diccionario = {
                        "token": tokenD,
                        "linea": lineaD,
                        "columna": columnaD
                    }

                    self.lista_token.append(diccionario)


                    self.index += len(token) - 1
                    self.columna += len(token) - 1
                    return estado_sig
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
                #print('COMBINACION -> ',i , '==', token[count])
                if str(i) == str(token[count]):
                    tokem_tmp += i  
                    count += 1 
                else:
                    #print('ERROR1')
                    return False
                    #return None
                
            print(f'\nENCONTRE --> {tokem_tmp} <--\n')
            #return 
            #return tokem_tmp
            return tokem_tmp == token
        except:
            #print('ERROR2')
            return False
            #return None

    #analizar cadena para las funciones (de un solo parametro)
    def _analizarCadena(self):
        estado_aux = ""
        tmp = self.index
        cadena = ""
        while self.lineas[tmp] != "":
            
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[tmp] == '\n':
                self.fila + self.fila + 1
                return 'ERROR'
            
            elif self.lineas[tmp] == '"'and estado_aux == '':
                print("INICIO")
                estado_aux = "INICIO"
            elif self.lineas[tmp] == '"' and estado_aux == 'INICIO':
                print("fin")
                return [cadena, tmp]
            elif estado_aux == 'INICIO':
                cadena += self.lineas[tmp]
                print(f'Cadena) - {self.lineas[tmp] } | FILA - {self.fila}  | COLUMNA - {self.columna}')

            #INCREMENTAR POSICION
            if tmp < len(self.lineas) - 1:
                tmp +=1
                self.columna = self.columna+1
            else:
                break

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
                parametro = ''
                valor = 0
                funciones = ['#', "'''", "imprimir", 'Imprimirln']
                #S0 -> # S_01|''' S_01|imprimir S_01|imprimirlnS_01
                for i in funciones:
                    estado_actual = self._token(i, 'S0', 'S_01')
                    if estado_actual == "S_01":
                        instruccion = i
                        if i == '#':
                            self._comentarioSimple()
                            estado_actual = 'S0'

                        elif i == "'''":
                            self._comentarioMulti()
                            estado_actual = 'S0'

                        elif i == "imprimir" or i == "Imprimirln":
                            self.index = self.index + 1

                            # S25 -> ( S26
                            if estado_actual == 'S_01':
                                estado_actual = self._token('(', 'S_01', 'S_02')

                            if estado_actual == 'S_02':
                                self.index = self.index+1
                                result = self._analizarCadena()
                                parametro = result[0]
                                #print('--->', parametro ,'<---')
                                #print('--->', len(parametro) ,'<---')
                                
                                self.index = result[1]
                                estado_actual = 'S_03'

                            if estado_actual == 'S_03':
                                self.index = self.index +1
                                estado_actual = self._token(')', 'S_03', 'S_04')

                            if estado_actual == 'S_04':
                                self.index = self.index + 1
                                estado_actual = self._token(';', 'S_04', 'S_05')

                            if estado_actual == 'S_05':
                                self.haciendo_laFuncion(i,parametro,valor)
                                self.index = self.index + 1
                                estado_actual = "S0"
                        break
                    else:
                        estado_actual = self._token('Claves', 'S0', 'S1')
                        if estado_actual == 'S1':
                            break
                

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
                parametro = ''
                valor = 0
                funciones = ['#', "'''", "imprimir", 'Imprimirln']
                for i in funciones:
                    estado_actual = self._token(i, 'S9', 'S_01')
                    if estado_actual == "S_01":
                        if i == '#':
                            self._comentarioSimple()
                            estado_actual = 'S9'

                        elif i == "'''":
                            self._comentarioMulti()
                            estado_actual = 'S9'

                        elif i == "imprimir" or i == "Imprimirln":
                            self.index = self.index + 1

                            # S25 -> ( S26
                            if estado_actual == 'S_01':
                                estado_actual = self._token('(', 'S_01', 'S_02')

                            if estado_actual == 'S_02':
                                self.index = self.index+1
                                result = self._analizarCadena()
                                parametro = result[0]
                                print('--->', parametro ,'<---')
                                print('--->', len(parametro) ,'<---')
                                
                                self.index = result[1]
                                estado_actual = 'S_03'

                            if estado_actual == 'S_03':
                                self.index = self.index +1
                                estado_actual = self._token(')', 'S_03', 'S_04')

                            if estado_actual == 'S_04':
                                self.index = self.index + 1
                                estado_actual = self._token(';', 'S_04', 'S_05')

                            if estado_actual == 'S_05':
                                self.haciendo_laFuncion(i,parametro,valor)
                                self.index = self.index + 1
                                estado_actual = "S9"
                        break
                    else:
                        estado_actual = self._token('Registros', 'S9', 'S10')
                        if estado_actual == 'S10':
                            break
                
            

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
        #mientras no sea vacio se sale
        while self.lineas[self.index+1] != "":
            print(f'CC) CARACTER - {self.lineas[self.index] } | FILA - {self.fila}  | COLUMNA - {self.columna}')
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
            #S6 -> , S7
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

                funciones = ['#', "'''"]

                for i in funciones:
                    estado_actual = self._token(i, 'S0', 'S_01')
                    if estado_actual == "S_01":
                        instruccion = i
                        if i == '#':
                            self._comentarioSimple()
                            estado_actual = 'S12'

                        elif i == "'''":
                            self._comentarioMulti()
                            estado_actual = 'S12'
                        break
                    else:
                        estado_actual = self._token('{', 'S12', 'S13')
                        if estado_actual == 'S13':
                            break
            

                """# S12 -> { S13 (llave de inico)
                if estado_actual == 'S12':
                    estado_actual = self._token('{', 'S12', 'S13')"""

            #aqui debo guardar los valores
            # S13 -> valores S14
            elif estado_actual == 'S13':
                estado_sig = self._infoRegistros(estado_actual, lista_temp)
                #retornar S14
                #print(lista_temp)
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
        instruccion = ''
        parametro = ''
        valor = 0

        #S24
        estado_actual = estadoActual
        #mientras no sea vacio se sale
        while self.lineas[self.index] != "":
            
            print(f'Funciones) CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 1

            elif self.lineas[self.index] == '<':
                #S7 -> ] S8
                return
            else:
                self.columna +=1

            # S24 -> funciones S25
            if estado_actual == 'S24':
                
                funcionesCC = ['#', "'''"]

                for i in funcionesCC:
                    estado_actual = self._token(i, 'S24', 'S_01')
                    if estado_actual == "S_01":
                        if i == '#':
                            self._comentarioSimple()
                            estado_actual = 'S24'

                        elif i == "'''":
                            self._comentarioMulti()
                            estado_actual = 'S24'
                        break
                    else:
                        #estado_actual = 'ERROR'
                        #iterar para todas las funciones
                        #imprimir, imprimirln, conteo, promedio, contarsi, datos, sumar, max, min, exportarReporte
                        funciones = ['imprimir', 'Imprimirln', 'conteo', 'promedio', 'contarsi', 'datos', 'sumar', 'max', 'min', 'exportarReporte']
                        
                        for i in funciones:
                            estado_actual = self._token(i, 'S24', 'S25')
                            
                            if estado_actual != "ERROR":
                                instruccion = i
                                break
                        if estado_actual == 'S25':
                            break


                """estado_actual = self._token('#', 'S24', 'comentario')
                if estado_actual == 'comentario':
                    self._comentarioSimple()
                    estado_actual = 'S24'
                else:
                    
                    #iterar para todas las funciones
                    #imprimir, imprimirln, conteo, promedio, contarsi, datos, sumar, max, min, exportarReporte
                    funciones = ['imprimir', 'Imprimirln', 'conteo', 'promedio', 'contarsi', 'datos', 'sumar', 'max', 'min', 'exportarReporte', '#']
                    
                    for i in funciones:
                        estado_actual = self._token(i, 'S24', 'S25')
                        
                        if estado_actual != "ERROR":
                            instruccion = i
                            break"""



            # S25 -> ( S26
            elif estado_actual == 'S25':
                estado_actual = self._token('(', 'S25', 'S26')
                #         1                    2                      3                   4                 5               6               7
                if (instruccion == "imprimir") or (instruccion == "Imprimirln") or (instruccion== "promedio") or (instruccion == "sumar") or (instruccion == "max") or (instruccion== "min") or (instruccion == "exportarReporte"):
                    estado_actual = 'S26'

                #           1                    2
                elif (instruccion == "conteo") or (instruccion == "datos"):
                    estado_actual = 'S27'

                #           1
                elif (instruccion == "contarsi"):
                    estado_actual = 'S26'

            # S4 -> cadena S5
            elif estado_actual == 'S26':
                result = self._analizarCadena()
                parametro = result[0]
                #print('--->', parametro ,'<---')
                #print('--->', len(parametro) ,'<---')
                
                self.index = result[1]
                estado_actual = 'S27'


            elif estado_actual == 'S27':
                estado_actual = self._token(')', 'S27', 'S28')
                if estado_actual == 'ERROR':
                    estado_actual = 'S27'
                    estado_actual = self._token(',', 'S27', 'S_28')

            elif estado_actual == 'S28':
                estado_actual = self._token(';', 'S28', 'S29')

            elif estado_actual == 'S_28':
                #leer un numero y retornar el siguiente estado de de cierre de parentecis "S27"
                # Llamada a la función
                palabra = ''
                estado_sig, valor = self._parametro2(estadoActual, palabra)
                
                print('palabra: ', valor)

                if estado_sig == 'S27':
                    estado_actual = estado_sig
                    self.index =self.index-1


            elif estado_actual == 'S29':
                self.haciendo_laFuncion(instruccion,parametro,valor)
                # Aqui vuelvo recursivo para que lea todas las funciones
                estado_actual = 'S24'
                self.index +=1
                self._funciones(estado_actual)

            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _parametro2(self, estadoActual, valor):
        estado_actual = estadoActual
        palabra = ""  # Inicializa una cadena vacía para almacenar la palabra leída

        while self.index < len(self.lineas):
            print(f'Parametro) CARACTER - {self.lineas[self.index]} | ESTADO - {estado_actual} | FILA - {self.fila} | COLUMNA - {self.columna}')

            if self.lineas[self.index] == ')':
                if palabra:
                    valor = palabra.replace(' ', '')  # Almacena la palabra en la variable "valor" sin espacios
                return 'S27', valor

            # IDENTIFICAR SALTO DE LINEA
            elif self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna = 0
            else:
                palabra += self.lineas[self.index]  # Agrega el carácter a la palabra

            self.columna += 1

            # INCREMENTAR POSICIÓN
            if self.index < len(self.lineas) - 1:
                self.index += 1
            else:
                break

        return 'S27', valor  # Retorna 'S27' y el valor encontrado después del bucle

    def haciendo_laFuncion(self, instruccionO:str, campo, _valor):
        instruccion = instruccionO
        parametro = campo
        valor = _valor
        valor = int(valor)
        # le paso la lista de los registros que registro
        lista_lista = self.lista_resgistros

        # hago que la lista de listas se haga una sola lista de productos
        lista2 = Objetos(lista_lista)
        lista_de_productos = lista2.asignarValores()

        # con la lista de productos podre realizar las funciones
        # ya que tengo informacion para trabajar
        # creamos un objeto para poder acceder a la los metodos de la clase Funciones 
        # que son las funciones que tenemos que realizar
        funciones = Funciones(lista_de_productos)

        # Aqui se realizaran las funciones
        # para tipoA
        if instruccion == "imprimir":
            resultado = funciones.imprimir(parametro)
            print('>>>', resultado)
            

        elif instruccion == "Imprimirln":
            resultado = funciones.imprimirln(parametro)
            print('>>>', resultado)

        elif instruccion== "promedio":
            resultado = funciones.promedio(parametro)
            print('>>>', resultado)

        elif instruccion == "sumar":
            resultado = funciones.sumar(parametro)
            print('>>>', resultado)

        elif instruccion == "max":
            resultado = funciones.max(parametro)
            print('>>>', resultado)

        elif instruccion== "min":
            resultado = funciones.min(parametro)
            print('>>>', resultado)

        elif instruccion == "exportarReporte":
            resultado = funciones.exportarReporte(parametro,f'{parametro}.html')
            print('>>>', resultado)

        #           1                    2
        elif instruccion == "conteo":
            resultado = funciones.conteo()
            print('>>>', resultado)

        elif instruccion == "datos":
            resultado = funciones.datos()
            for elemento in resultado:
                print(elemento)

        #           1
        elif (instruccion == "contarsi"):
            resultado = funciones.contarsi(parametro, valor)
            print('>>>', resultado)

        if resultado:
            self.lista_resultados.append(resultado)
                    

    def _comentarioMulti(self):
            
            #mientras no sea vacio se sale
            while self.lineas[self.index] != "":
                
                print(f'CM) CARACTER - {self.lineas[self.index] } |  FILA - {self.fila}  | COLUMNA - {self.columna}')
                
                # IDENTIFICAR SALTO DE LINEA
                if self.lineas[self.index] == "'":
                    self.index = self.index + 1
                    if self.lineas[self.index] == "'":
                        self.index = self.index + 1
                        if self.lineas[self.index] == "'":
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

    def guardarErrores(self, token, fila, columna):
        self.ListaErrores.append({"token":token, "fila": fila, "columna":columna})




'''a = Analizador(contenido)
a._compile()

for resultados in a.lista_resultados:

    if type(resultados) == list:
        for lista in resultados:
            print('>>>', end="") 
            for valor in lista:
                print(" ",valor, end='  ')
            print()  # Imprimir una nueva línea entre cada lista
        print()
    else:
        print('>>>', resultados)'''
