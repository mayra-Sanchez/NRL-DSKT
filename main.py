import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageDraw, ImageTk
from ventanas.imagenes import imagenes
from ventanas.preprocesamiento import preprocesamiento
from ventanas.segmentacion_ventana import segmentacion_ventana
from ventanas.histograma import histograma
from ventanas.registro import registro


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
        self.botonSubir = Button(
            self, text="Imagenes", command=self.VentanaImagen)
        self.botonSubir.pack()
        self.botonSubir.config(bg="white")
        self.botonSubir.place(x=530, y=180)

        self.botonPreprocesamiento = Button(
            self, text="Pre-procesamiento", command=self.VentanaPreprocesamiento)
        self.botonPreprocesamiento.pack()
        self.botonPreprocesamiento.config(bg="white")
        self.botonPreprocesamiento.place(x=520, y=240)

        self.botonSegmentacion = Button(
            self, text="Segmentación", command=self.VentanaSegmentacion)
        self.botonSegmentacion.pack()
        self.botonSegmentacion.config(bg="white")
        self.botonSegmentacion.place(x=535, y=300)

        self.botonHistograma = Button(
            self, text="Histograma", command=self.VentanaHistograma)
        self.botonHistograma.pack()
        self.botonHistograma.config(bg="white")
        self.botonHistograma.place(x=535, y=360)

        self.botonRegistro = Button(self, text="Registro", command=self.VentanaRegistro)
        self.botonRegistro.pack()
        self.botonRegistro.config(bg="white")
        self.botonRegistro.place(x=535, y=420)

    def VentanaImagen(self):
        ventana_image = imagenes(self)

    def VentanaPreprocesamiento(self):
        ventana_image = preprocesamiento(self)

    def VentanaSegmentacion(self):
        ventana_image = segmentacion_ventana(self)

    def VentanaHistograma(self):
        ventana_image = histograma(self)

    def VentanaRegistro(self):
        ventana_image = registro(self)

if __name__ == "__main__":
    app = VentanaInicial()
    app.geometry("650x550")
    app.config(bg="grey")
    app.mainloop()
