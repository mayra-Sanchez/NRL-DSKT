import tkinter as tk
from tkinter import Label

class VentanaAyuda(tk.Toplevel):
    def __init__(self, parent, ayuda):
        super().__init__(parent)
        self.title("Ayuda")
        self.config(bg="grey")

        # Definir los componentes de la nueva ventana
        self.etiqueta = Label(self, text="Ayuda")
        self.etiqueta.pack()
        self.etiqueta.config(font=('Arial', 44))
        self.etiqueta.place(x=100, y=40)
        self.etiqueta.config(bg="grey")

        self.texto = Label(self, text=ayuda)
        self.texto.pack()
        self.texto.place(x=100, y=150)

        self.botonCerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        self.botonCerrar.pack()
        self.botonCerrar.place(x=400, y=300)

        self.geometry("650x550")