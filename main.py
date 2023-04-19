import tkinter as tk
from tkinter import Tk, Label, Button

class VentanaInicial:

	def __init__(self, master):
		self.master = master
		master.title("NRL-DSKT")
		self.etiqueta = Label(master, text="NRL-DSKT")
		self.etiqueta.pack()
		self.etiqueta.config(font=('Arial', 44))
		self.etiqueta.place(x=55, y=40)
		self.etiqueta.config(bg="grey")

		self.image = tk.PhotoImage(file="cerebro.png")
		self.labelImagen = Label(image=self.image)
		self.labelImagen.pack()
		self.labelImagen.place(x=10, y=150)
		self.labelImagen.config(bg="grey")

		self.botonSubir = Button(master, text="Subir imagen", command=self.abrir_ventana_imagen)
		self.botonSubir.pack()
		self.botonSubir.place(x=500, y=180)

		self.botonHistorial = Button(master, text="Historial", command=master.abrir_ventana_historial)
		self.botonHistorial.pack()
		self.botonHistorial.place(x=520, y=240)

		self.botonAyuda = Button(master, text="¿?", command=master.abrir_ventana_ayuda)
		self.botonAyuda.pack()
		self.botonAyuda.place(x=535, y=300)

root = Tk()
root.config(bg="grey")

miVentana = VentanaInicial(root)
root.mainloop()
