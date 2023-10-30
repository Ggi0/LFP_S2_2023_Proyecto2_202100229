
#Giovanni Saul Concohá Cax - 202100229
#Ggi0

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Para abrir el archivo .bizdat
def abrir_archivo():
    #abro archivos con cualquier externsión 
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.*")])
    if archivo:
        with open(archivo, 'r') as file:
            contenido = file.read()

            #colocar el contenido en el panel editable
            panel_izquierdo.delete('1.0', tk.END)
            panel_izquierdo.insert(tk.END, contenido)

# Función del botón para que funciones el analizador
def analizar_texto():
    texto = panel_izquierdo.get('1.0', tk.END)
    # lógica de análisis de texto

    # procesar 'texto' y mostrar los resultados en el panel derecho.
    panel_derecho.config(state=tk.NORMAL)
    panel_derecho.delete('1.0', tk.END)
    panel_derecho.insert(tk.END, f"Resultado del análisis:\n{texto}")
    
    # resultado del análisis .
    panel_derecho.config(state=tk.DISABLED)

# Función para generar los REPORTES
def generar_reporte():
    # Obtiene el contenido del panel derecho
    contenido_panel_derecho = panel_derecho.get('1.0', tk.END)

    name = str(input("Ej: nombre.html: "))
    # Crea un archivo HTML y escribe el contenido del panel derecho
    with open(name, "w") as archivo_html:
        name = name.replace(".html", "")
        contenido_html = (f"<html><body><pre>{name, contenido_panel_derecho}</pre></body></html>")
        archivo_html.write(contenido_html)

    # Indica que se ha generado el archivo
    print("Reporte HTML generado.")

# Funcion para realizar lo que diga el comboBox
def seleccionar(event):
    seleccion = combo_var.get()
    if seleccion == "Reportes de errores":
        print("Reportes de errores")
        generar_reporte()

    if seleccion == "Reporte de tokens":
        print("Reporte de tokens")
        #guardar()
        

    if seleccion == "Árbol":
        print("Árbol")
        #guardar_como()


def cerrar_aplicacion():
    print('Cerrando programa')
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PROYECTO 2")
ventana.geometry("800x630")

# Crear un marco para los paneles de texto
marco_paneles = tk.Frame(ventana)
marco_paneles.grid(row=1, column=0, columnspan=2)

# Crear paneles de texto
panel_izquierdo = tk.Text(marco_paneles, height=40, width=70)
panel_derecho = tk.Text(marco_paneles, height=40, width=40)
panel_derecho.config(state=tk.DISABLED)

panel_izquierdo.grid(row=0, column=0)
panel_derecho.grid(row=0, column=1)

# Crear un nuevo marco para los botones y la etiqueta
marco_botones = tk.Frame(ventana)
marco_botones.grid(row=0, column=0, columnspan=4, pady=(0, 10))

# Etiqueta "Proyecto 2 - 202100229" sin espacio interno
etiqueta = tk.Label(marco_botones, text="Proyecto 2 - 202100229", font=("Arial black", 15))
etiqueta.grid(row=0, column=0, padx=20, pady=10, ipadx=20, ipady=0, sticky="w")

# Crear botones en la esquina superior derecha sin espacio interno
boton_abrir = tk.Button(marco_botones, text="Abrir", command=abrir_archivo)
boton_analizar = tk.Button(marco_botones, text="Analizar", command=analizar_texto)

boton_abrir.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky="e")
boton_analizar.grid(row=0, column=2, padx=0, pady=0, ipadx=0, ipady=0, sticky="e")
#boton_reportes.grid(row=0, column=3, padx=0, pady=0, ipadx=0, ipady=0, sticky="e")

# Variable para almacenar la selección del ComboBox
combo_var = tk.StringVar()
combo_var.set("ERRORES") # Valor inicial en el ComboBox

# -----------------------------ComboBox
combo = ttk.Combobox(marco_botones, textvariable=combo_var)
combo['values'] = ('Reportes de errores', 'Reporte de tokens', 'Árbol')
combo.grid(row=0, column=3, padx=0, pady=0, ipadx=0, ipady=0, sticky="e") 

# Asociar la función de selección al evento <<ComboboxSelected>>
combo.bind("<<ComboboxSelected>>", seleccionar)

# Crear un botón "Cerrar" en la parte inferior
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_aplicacion)
boton_cerrar.grid(row=2, column=0, columnspan=4, pady=(10, 0))

ventana.mainloop()

