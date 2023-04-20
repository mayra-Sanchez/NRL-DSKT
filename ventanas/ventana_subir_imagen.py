import tkinter as tk
from tkinter import Tk, Label, Button

class ventanaSubirImagen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Subir imagen")
        self.config(bg="grey")

        # Definir los componentes de la nueva ventana
        self.etiqueta = Label(self, text="Subir imagen")
        self.etiqueta.pack()
        self.etiqueta.config(font=('Arial', 44))
        self.etiqueta.place(x=100, y=40)
        self.etiqueta.config(bg="grey")

        self.entry = tk.Entry(self)
        self.entry.pack()
        self.entry.place(x=200, y=200)

        self.botonCargar = Button(self, text="Cargar", command=self.cargar_imagen)
        self.botonCargar.pack()
        self.botonCargar.place(x=300, y=250)

        self.botonCerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        self.botonCerrar.pack()
        self.botonCerrar.place(x=400, y=300)

        self.geometry("650x550")

    def cargar_imagen(self):
        # código para cargar la imagen
        pass