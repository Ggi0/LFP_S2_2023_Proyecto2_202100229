# Analizador léxico para tu lenguaje simple
def lexer(codigo_fuente):
    tokens = []
    codigo_fuente = codigo_fuente.replace('\n', ' ')  # Elimina saltos de línea
    codigo_fuente = codigo_fuente.replace('\t', ' ')  # Elimina tabulaciones
    palabra = ''
    in_cadena = False

    for char in codigo_fuente:
        if char == '"':
            if in_cadena:
                tokens.append(('CADENA', palabra))
                palabra = ''
                in_cadena = False
            else:
                in_cadena = True
                palabra += char
        elif char.isalnum() or char == '_':
            palabra += char
        elif palabra:
            tokens.append(('PALABRA', palabra))
            palabra = ''
        if char in ' \t()[]{};,=*':
            if palabra:
                tokens.append(('PALABRA', palabra))
                palabra = ''
            if char.strip():
                tokens.append(('SIMBOLO', char))

    return tokens

# Ejemplo de código fuente
codigo_fuente = """'''
# COMENTARIO 
'''
claves = ["codigo", "producto", "precio_compra", "precio_venta", "stock"]
'''

# Llamada al analizador léxico
tokens_encontrados = lexer(codigo_fuente)

# Imprimir los tokens encontrados
for token, valor in tokens_encontrados:
    print(f'Token: {token}, Valor: {valor}')
"""