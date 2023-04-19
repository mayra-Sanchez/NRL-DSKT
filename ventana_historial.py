import tkinter as tk
from tkinter import Tk, Label, Button

class VentanaHistorial(tk.Toplevel):
    def __init__(self, parent, historial):
        super().__init__(parent)
        self.title("Historial de imágenes")
        self.config(bg="grey")

        # Definir los componentes de la nueva ventana
        self.etiqueta = Label(self, text="Historial de imágenes")
        self.etiqueta.pack()
        self.etiqueta.config(font=('Arial', 44))
        self.etiqueta.place(x=100, y=40)
        self.etiqueta.config(bg="grey")

        self.lista_imagenes = tk.Listbox(self, width=40, height=10)
        self.lista_imagenes.pack()
        self.lista_imagenes.place(x=200, y=150)

        for imagen in historial:
            self.lista_imagenes.insert(tk.END, imagen)

        self.botonCerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        self.botonCerrar.pack()
        self.botonCerrar.place(x=400, y=400)

        self.geometry("650x550")