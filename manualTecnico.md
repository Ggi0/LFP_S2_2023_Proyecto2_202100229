# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION
## Proyecto #2
### 2do Semestre
```js
Universidad San Carlos de Guatemala
Programador: Giovanni Saul Concohá Cax
Carne: 202100229
Correo: 3035111680110@ingenieria.usac.edu.gt
```
---
# Manual técnico

# BizData

---
## Descripción del Proyecto

El proyecto "BizData" (Business Data Analysis) es una plataforma destinada a brindar a las pequeñas empresas las herramientas necesarias para tomar decisiones informadas y estratégicas a través del análisis detallado de sus datos comerciales. El objetivo principal de este proyecto es permitir que estas empresas aprovechen sus datos para obtener información valiosa y, en última instancia, mejorar su rendimiento y competitividad en el mercado.

El estudiante de Lenguajes Formales y de Programación tiene la tarea de desarrollar un analizador léxico y sintáctico utilizando el lenguaje de programación Python. Este analizador está diseñado específicamente para procesar datos empresariales estructurados que se presentan en un formato especializado con la extensión ".bizdata". El proceso de análisis implica la capacidad de cargar y examinar estos datos en busca de patrones, tendencias y métricas clave que puedan ayudar a las empresas a tomar decisiones más informadas.

## Objetivos
* Objetivo General
    * Desarrollar una solución de software que permita a las pequeñas empresas analizar datos comerciales en formato ".bizdata" a través de la implementación de un analizador léxico y sintáctico utilizando conceptos de gramáticas independientes de contexto y árboles de derivación, con el fin de facilitar la toma de decisiones estratégicas basadas en datos.
* Objetivos Específicos
    * Desarrollar un analizador sintáctico que utilice gramáticas independientes de contexto y árboles de derivación para interpretar y comprender la estructura de los datos en formato ".bizdata", permitiendo la extracción de información significativa y la generación de informes analíticos.
    * Implementar un analizador léxico en Python que sea capaz de identificar y tokenizar los elementos y estructuras de datos presentes en archivos ".bizdata", permitiendo la preparación de datos para su análisis posterior.
---
# CLASES(  ):

La clase `Analizador` es un componente fundamental para analizar y procesar archivos de entrada con formato ".bizdata". A continuación, se describe la clase de manera que pueda ser incluida en un manual técnico:

**Clase: Analizador**

**Descripción:**
El `Analizador` es una clase que se utiliza para analizar archivos de entrada en formato ".bizdata" y procesar la información contenida en ellos. Esta clase implementa un analizador léxico y sintáctico en Python, que identifica elementos clave y registros en los archivos ".bizdata" y permite realizar funciones específicas basadas en las claves y valores encontrados.

**Atributos:**
- `lineas`: Almacena la entrada de texto que se va a analizar.
- `index`: Lleva un seguimiento de la posición actual en el texto de entrada.
- `fila`: Registra la línea actual del texto.
- `columna`: Registra la columna actual del texto.
- `claves`: Lista que guarda los nombres de las claves encontradas en el archivo.
- `lista_registros`: Lista que contiene listas de los valores de los registros, que se transformarán en objetos de tipo "Productos".
- `lista_resultados`: Lista donde se almacenan los resultados de las funciones procesadas.
- `lista_token`: Lista que almacena información sobre los tokens identificados durante el análisis.
- `ListaErroresS`: Lista para guardar errores sintácticos.
- `ListaErroresL`: Lista para guardar errores léxicos.

**Métodos:**
- `_token(token, estado_actual, estado_sig)`: Este método se utiliza para identificar y analizar tokens en el texto de entrada. Dependiendo del token proporcionado y el estado actual, se determina si se debe avanzar al estado siguiente o si se produce un error.
- `_juntar(_index, _count)`: Este método toma una posición inicial y un recuento y concatena los caracteres correspondientes para formar una cadena.
- `_analizar(token, texto)`: Compara un token con una cadena de texto y determina si hay una coincidencia completa entre ambos.
- `_analizarCadena()`: Este método se utiliza para analizar cadenas de caracteres y extraer información entre comillas dobles.
- `_compile()`: Método principal que coordina el análisis léxico y sintáctico del archivo ".bizdata". Implementa una máquina de estados para procesar la entrada.
- `_comentarioSimple()`: Maneja comentarios de una sola línea en el archivo.
- `_claves(estadoActual)`: Analiza las claves presentes en el archivo ".bizdata" y las almacena en la lista "claves".
- `_info(estadoActual, claves)`: Extrae la información relacionada con las claves en el archivo.
- `_registros(estadoActual)`: Analiza los registros en el archivo y almacena la información en la lista de registros.
- `_infoRegistros(estadoActual, valores)`: Extrae la información relacionada con los registros.
- `_funciones(estadoActual)`: Identifica y procesa funciones encontradas en el archivo ".bizdata".
- `_parametro2(estadoActual, valor)`: Analiza parámetros en las funciones y recopila la información.
- `haciendo_laFuncion(instruccionO, campo, valor)`: Ejecuta las funciones identificadas en el archivo y almacena los resultados en la lista de resultados.
- `_comentarioMulti()`: Maneja comentarios de varias líneas en el archivo.
- `guardarErrores(token, fila, columna)`: Registra errores léxicos y sintácticos identificados durante el análisis.

**Uso:**
1. Cree una instancia de la clase `Analizador`, proporcionando la entrada en formato ".bizdata" como argumento al constructor.
2. Llame al método `_compile()` para iniciar el análisis del archivo.
3. Acceda a los resultados procesados a través de la lista `lista_resultados`.

La clase `Analizador` es una herramienta esencial para analizar y procesar archivos ".bizdata" y realizar diversas operaciones basadas en los datos contenidos en estos archivos. Sus métodos permiten identificar claves, registros, funciones y realizar análisis profundo de los datos comerciales.

---
**Clase Productos**

La clase `Productos` es un componente esencial de una aplicación de gestión de inventario o comercio, diseñada para representar y gestionar información sobre productos. Esta clase se utiliza para crear objetos que contienen detalles específicos sobre un producto, como su código, nombre, precios de compra y venta, y el stock disponible. La información se almacena y se puede acceder y manipular a través de los métodos proporcionados.

**Métodos:**

- `__init__(self, codigo, producto, precio_compra, precio_venta, stock)`: Este método constructor se utiliza para crear un objeto `Productos`. Toma como argumentos los atributos clave de un producto, como el código, el nombre del producto, el precio de compra, el precio de venta y el stock. Estos valores se asignan a las propiedades del objeto para su posterior acceso y manipulación.

- `imprimir_informacion(self)`: Este método se encarga de imprimir en la consola la información detallada de un producto. Muestra el código del producto, el nombre, el precio de compra, el precio de venta y el stock disponible. La información se presenta de manera legible y organizada.


La clase `Productos` es fundamental en la gestión de inventario y ventas, permitiendo la representación y manipulación de información de productos, lo que facilita el seguimiento de inventario y la gestión de ventas en una aplicación.

---
**Clase Objetos - Creación de Objetos a partir de Listas de Datos**

La clase `Objetos` es una parte fundamental de una aplicación que se encarga de procesar y transformar datos contenidos en una lista en objetos. Esta clase permite convertir una lista de listas en una colección de objetos de tipo `Productos` con propiedades específicas, lo que facilita la manipulación y gestión de dichos datos. A continuación, se describen los elementos clave de esta clase:

**Métodos:**

- `__init__(self, entrada: list)`: El método constructor recibe una lista `entrada` que contiene listas internas con datos de productos. La variable `lista_lista` almacena esta lista de listas, que posteriormente se procesará para crear objetos `Productos`.

- `asignarValores(self)`: Este método se encarga de recorrer las listas internas contenidas en `self.lista_lista` y, para cada lista interna, crea un objeto `Productos` con los datos específicos que representan un producto. Luego, agrega estos objetos a la lista `lista_de_productos`. Los datos en las listas internas se convierten a tipos de datos apropiados, como enteros y flotantes, antes de crear los objetos. El método devuelve la lista `lista_de_productos` con los objetos creados.

Esta clase es útil cuando se necesita convertir datos de productos contenidos en listas en objetos que faciliten su manipulación y gestión. Permite la creación eficiente de objetos `Productos` a partir de datos preexistentes, lo que es esencial en la gestión de inventario y ventas en una aplicación.

---
**Clase Funciones - Procesamiento y Análisis de Datos de Productos**

La clase `Funciones` es una parte esencial de una aplicación diseñada para procesar y analizar datos de productos. Proporciona una variedad de métodos que permiten realizar diversas operaciones y cálculos sobre una lista de objetos de la clase `Productos`. A continuación, se describen los elementos clave de esta clase:

**Métodos:**

- `__init__(self, entrada: list)`: El método constructor recibe una lista `entrada` que contiene objetos de la clase `Productos` o sus equivalentes. Estos objetos representan productos con propiedades específicas.

- `imprimir(self, cadena: str)`: Este método recibe una cadena `cadena` y simplemente la devuelve sin ningún procesamiento adicional.

- `imprimirln(self, cadena: str = "")`: Similar al método `imprimir`, este método recibe una cadena `cadena` y devuelve la misma cadena. Opcionalmente, agrega un carácter de nueva línea al final de la cadena.

- `conteo(self)`: Calcula y devuelve el número total de registros (productos) en la lista.

- `promedio(self, clave: str)`: Calcula el promedio de los valores de un atributo específico (identificado por `clave`) en la lista de productos y lo devuelve. Si la lista está vacía o el atributo no existe en los objetos, devuelve 0.

- `contarsi(self, clave: str, valor)`: Cuenta cuántos productos en la lista tienen un valor específico en un atributo determinado (identificado por `clave`) y devuelve la cantidad. Si la lista está vacía o el atributo no existe en los objetos, devuelve 0.

- `datos(self)`: Transforma los datos de la lista de productos en una estructura de lista bidimensional, donde la primera fila contiene los nombres de los atributos y las filas subsiguientes representan los registros de productos.

- `sumar(self, clave: str)`: Calcula la suma de los valores de un atributo específico (identificado por `clave`) en la lista de productos y la devuelve. Si la lista está vacía o el atributo no existe en los objetos, devuelve 0.

- `max(self, clave: str)`: Encuentra el valor máximo en un atributo específico (identificado por `clave`) en la lista de productos y lo devuelve. Si la lista está vacía o el atributo no existe en los objetos, devuelve `None`.

- `min(self, clave: str)`: Encuentra el valor mínimo en un atributo específico (identificado por `clave`) en la lista de productos y lo devuelve. Si la lista está vacía o el atributo no existe en los objetos, devuelve `None`.

- `exportarReporte(self, titulo, nombre_archivo)`: Genera un archivo HTML que presenta los datos de la lista de productos en formato tabular. El archivo incluye encabezados de tabla y filas de datos. También se encarga de dar formato a la tabla. Si la lista está vacía, muestra un mensaje de advertencia en la consola.

---
# Transiciones

1. `S0 -> Claves S1 | # S_01| ''' S_01| imprimir S_01| imprimirln S_01`: Esta línea indica que el estado inicial `S0` puede ser seguido por la palabra clave `Claves` y luego el estado `S1`. También puede ser seguido por un comentario (indicado por `#` o `'''`), o las palabras clave `imprimir` o `imprimirln`, cada una seguida por el estado `S1`.

2. `S1 -> = S2`: Este es un paso de asignación. Después de la palabra clave `Claves`, se espera un signo igual (`=`), seguido por el estado `S2`.

3. `S2 -> [ S3`: Aquí se espera un corchete de apertura (`[`), seguido por el estado `S3`.

4. `S3 -> " S5 (comillas de inicio)`: Se espera una comilla de inicio, seguida por el estado `S5`.

5. `S5 -> clave S6`: Aquí se espera una clave, seguida por el estado `S6`.

6. `S6 -> " S7 (comillas de cierre)`: Se espera una comilla de cierre, seguida por el estado `S7`.

7. `S7 -> , S3 | ] S9`: Después de la comilla de cierre, se puede esperar una coma y luego volver al estado `S3` para otra clave, o un corchete de cierre (`]`) seguido por el estado `S9`.


8. `S9 -> Registros S10 | # S_01| ''' S_01| imprimir S_01| imprimirln S_01`: Similar a la primera línea, pero esta vez con la palabra clave `Registros` seguida por el estado `S10`. También puede ser seguido por un comentario o las palabras clave `imprimir` o `imprimirln`.

9. `S10 -> = S11`: Este es otro paso de asignación. Después de la palabra clave `Registros`, se espera un signo igual (`=`), seguido por el estado `S11`.

10. `S11 ->[ S12`: Aquí se espera un corchete de apertura (`[`), seguido por el estado `S12`.

11. `S12 -> { S13 (llave de inicio)| # S_01| ''' S_01`: Se espera una llave de inicio, seguida por el estado `S13`. También puede ser seguido por un comentario.

12. `S13 -> valor S14`: Aquí se espera un valor, seguido por el estado `S14`.

13. `S14 -> , S13| } S15`: Después del valor, se puede esperar una coma y luego volver al estado `S13` para otro valor, o una llave de cierre (`}`) seguida por el estado `S15`.

14. `S15 -> ] S16 | { S12`: Después de la llave de cierre, se puede esperar un corchete de cierre (`]`) seguido por el estado `S16`, o una llave de apertura (`{`) para más valores en el registro.

15. `S16 -> funciones S17| # S_01| ''' S_01| E`: Aquí se espera la palabra clave `funciones` seguida por el estado `S17`, o un comentario, o el fin del archivo (indicado por `E`).

16. `S17 -> epsilon`: Finalmente, después de la palabra clave `funciones`, se llega al final de la secuencia (indicado por `epsilon`), lo que significa que no hay más entrada.

---
