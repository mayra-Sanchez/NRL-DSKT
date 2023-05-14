import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageDraw, ImageTk
from ventanas.ventana_ayuda import VentanaAyuda
from ventanas.ventana_historial import VentanaHistorial
from ventanas.ventana_subir_imagen import ventanaSubirImagen

class VentanaInicial(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("NRL-DSKT")
        self.etiqueta = Label(self, text="NRL-DSKT")
        self.etiqueta.pack()
        self.etiqueta.config(font=('Arial', 44))
        self.etiqueta.place(x=100, y=40)
        self.etiqueta.config(bg="grey")

        self.image = tk.PhotoImage(file="Resources/cerebro.png")
        self.labelImagen = Label(image=self.image)
        self.labelImagen.pack()
        self.labelImagen.place(x=10, y=150)
        self.labelImagen.config(bg="grey")

        # Definir los componentes de la interfaz
        self.botonSubir = Button(self,text="Subir", command=self.VentanaImagen)
        self.botonSubir.pack()
        self.botonSubir.config(bg="white")		
        self.botonSubir.place(x=530, y=180)

        self.botonHistorial = Button(self, text="Historial", command=self.mostrar_historial)
        self.botonHistorial.pack()
        self.botonHistorial.config(bg="white")
        self.botonHistorial.place(x=520, y=240)

        self.botonAyuda = Button(self, text="¿?", command=self.mostrar_ayuda)
        self.botonAyuda.pack()
        self.botonAyuda.config(bg="white")
        self.botonAyuda.place(x=535, y=300)
    
    def VentanaImagen(self):
        ventana_image = ventanaSubirImagen(self)

    def mostrar_historial(self):
        historial = ["imagen1.png", "imagen2.png", "imagen3.png"]  # Aquí iría el código para obtener el historial de imágenes
        ventana_historial = VentanaHistorial(self,historial)

    def mostrar_ayuda(self):
        ayuda = "Esta es la ventana de ayuda. Aquí puedes encontrar información sobre cómo usar la aplicación."
        ventana_ayuda = VentanaAyuda(self, ayuda)

if __name__ == "__main__":
    app = VentanaInicial()
    app.geometry("650x550")
    app.config(bg="grey")
    app.mainloop()
