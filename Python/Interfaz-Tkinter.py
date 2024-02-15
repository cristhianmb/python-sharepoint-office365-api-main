import tkinter as tk
from tkinter import filedialog
import pandas as pd

def procesar_archivos(ruta_origen, ruta_destino):
    # Aquí va tu lógica de procesamiento con Pandas
    # Por ahora, solo imprime las rutas para verificar
    print(f"Ruta de archivo origen: {ruta_origen}")
    print(f"Ruta de archivo destino: {ruta_destino}")
    # Agrega tu lógica de Pandas para cargar, transformar y guardar el archivo Excel

def seleccionar_archivo_origen():
    ruta_origen = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos de Excel", "*.xlsx;*.xls")])
    entry_ruta_origen.delete(0, tk.END)
    entry_ruta_origen.insert(0, ruta_origen)

def seleccionar_carpeta_destino():
    ruta_destino = filedialog.askdirectory(title="Seleccionar carpeta destino")
    entry_ruta_destino.delete(0, tk.END)
    entry_ruta_destino.insert(0, ruta_destino)

def procesar():
    ruta_origen = entry_ruta_origen.get()
    ruta_destino = entry_ruta_destino.get()
    procesar_archivos(ruta_origen, ruta_destino)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesador de Archivos")

# Crear y colocar widgets
label_ruta_origen = tk.Label(ventana, text="Ruta de archivo origen:")
label_ruta_origen.grid(row=0, column=0, padx=10, pady=10)

entry_ruta_origen = tk.Entry(ventana, width=40)
entry_ruta_origen.grid(row=0, column=1, padx=10, pady=10)

button_seleccionar_origen = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo_origen)
button_seleccionar_origen.grid(row=0, column=2, padx=10, pady=10)

label_ruta_destino = tk.Label(ventana, text="Ruta de archivos destino:")
label_ruta_destino.grid(row=1, column=0, padx=10, pady=10)

entry_ruta_destino = tk.Entry(ventana, width=40)
entry_ruta_destino.grid(row=1, column=1, padx=10, pady=10)

button_seleccionar_destino = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta_destino)
button_seleccionar_destino.grid(row=1, column=2, padx=10, pady=10)

button_procesar = tk.Button(ventana, text="Procesar", command=procesar)
button_procesar.grid(row=2, column=0, columnspan=3, pady=20)

# Iniciar el bucle principal
ventana.mainloop()
