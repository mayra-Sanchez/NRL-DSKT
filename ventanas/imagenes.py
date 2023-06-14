import tkinter as tk
import os
from tkinter import Tk, filedialog, Scrollbar
from tkinter import ttk, messagebox
import shutil
import nibabel as nib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class imagenes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Imagenes")
        self.config(bg="grey")
        self.geometry("1050x610")

        self.etiqueta = tk.Label(self, text="NRL-DSKT")
        self.etiqueta.pack()
        self.etiqueta.config(font=('Times new roman', 35))
        self.etiqueta.place(x=200, y=30)
        self.etiqueta.config(bg="grey")

        # Carpeta de pacientes
        def obtener_carpetas():
            # Ruta de la carpeta de recursos de tu aplicación
            carpeta_recursos = "./resources/images"
            carpetas = []
            for elemento in os.listdir(carpeta_recursos):
                ruta_elemento = os.path.join(carpeta_recursos, elemento)
                if os.path.isdir(ruta_elemento):
                    carpetas.append(elemento)
            return carpetas
        
        self.current_image = None  # Track the currently displayed image

        # Imagenes de pacientes
        def seleccionar_imagen(event):
            global data, ruta_imagen
            imagen_seleccionada = dropdown_contenido.get()
            print("imagen seleccionada: ", imagen_seleccionada)
            if imagen_seleccionada:
                carpeta_seleccionada = dropdown.get()
                ruta_imagen = os.path.join(
                    "./resources/images", carpeta_seleccionada, imagen_seleccionada)

                # Load the NIfTI image using nibabel
                img = nib.load(ruta_imagen)
                data = img.get_fdata()

                # Display the image on the canvas
                plt.figure(figsize=(4.5, 4.5))
                plt.imshow(data[:,:,0])
                plt.axis('on')

                if hasattr(self, "canvas_fig_agg"):
                    self.canvas_fig_agg.get_tk_widget().destroy()
                    del self.canvas_fig_agg

                self.canvas_fig_agg = FigureCanvasTkAgg(plt.gcf(), master=self.canvas)
                self.canvas_fig_agg.draw()
                self.canvas_fig_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def obtener_contenido(carpeta_seleccionada):
            carpeta_recursos = "./resources/images/" + carpeta_seleccionada
            contenido = []
            for elemento in os.listdir(carpeta_recursos):
                ruta_elemento = os.path.join(carpeta_recursos, elemento)
                if os.path.isfile(ruta_elemento):
                    contenido.append(elemento)
            return contenido

        self.imagen =  tk.StringVar()
        
        def seleccionar_carpeta(event):
            seleccion = dropdown.get()
            print("Carpeta seleccionada:", seleccion)

            # Obtener el contenido de la carpeta seleccionada
            contenido = obtener_contenido(seleccion)

            # Configurar los valores del segundo menú desplegable con el contenido
            dropdown_contenido["values"] = contenido

            # Limpiar la variable de la imagen seleccionada
            self.imagen.set("")

        def crear_carpeta():
            nueva_carpeta = tk.simpledialog.askstring(
                "Crear carpeta", "Ingrese el nombre de la nueva carpeta:")
            if nueva_carpeta:
                carpeta_recursos = "./resources/images"
                ruta_nueva_carpeta = os.path.join(
                    carpeta_recursos, nueva_carpeta)

                # Verificar si la carpeta ya existe
                if os.path.exists(ruta_nueva_carpeta):
                    messagebox.showerror("Error", "La carpeta ya existe.")
                else:
                    # Crear la nueva carpeta
                    os.mkdir(ruta_nueva_carpeta)
                    messagebox.showinfo(
                        "Éxito", "La carpeta se ha creado correctamente.")
                    carpetas = obtener_carpetas()
                    dropdown["values"] = carpetas
            else:
                messagebox.showerror(
                    "Error", "Debe ingresar un nombre para la carpeta.")

        def subir_imagen():
            carpeta_seleccionada = dropdown.get()
            if carpeta_seleccionada:
                ruta_carpeta = os.path.join(
                    "./resources/images", carpeta_seleccionada)

                # Abrir el cuadro de diálogo de selección de archivos
                ruta_imagen = filedialog.askopenfilename()
                if ruta_imagen:
                    nombre_imagen = os.path.basename(ruta_imagen)
                    ruta_destino = os.path.join(ruta_carpeta, nombre_imagen)

                    # Mover la imagen a la carpeta correspondiente
                    shutil.move(ruta_imagen, ruta_destino)
                    messagebox.showinfo(
                        "Éxito", "La imagen se ha subido correctamente.")
                else:
                    messagebox.showerror(
                        "Error", "No se seleccionó ninguna imagen.")
            else:
                messagebox.showerror(
                    "Error", "Debe seleccionar una carpeta de paciente.")

        # Canvas para observar la imagen
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.place(x=100, y=100, width=450, height=450)

        # Pacientes
        self.labelCarpeta = tk.Label(self, text="Selecciona el paciente")
        self.labelCarpeta.pack()
        self.labelCarpeta.config(font=('Times new roman', 15))
        self.labelCarpeta.place(x=600, y=200)
        self.labelCarpeta.config(bg="grey")

        dropdown = ttk.Combobox(self)
        dropdown.bind("<<ComboboxSelected>>", seleccionar_carpeta)
        dropdown.pack()
        dropdown.place(x=800, y=200)

        carpetas = obtener_carpetas()
        dropdown["values"] = carpetas

        # Imagenes de pacientes
        self.labelImagenes = tk.Label(self, text="Selecciona la imagen")
        self.labelImagenes.pack()
        self.labelImagenes.config(font=('Times new roman', 15))
        self.labelImagenes.place(x=600, y=400)
        self.labelImagenes.config(bg="grey")

        dropdown_contenido = ttk.Combobox(self)
        dropdown_contenido.bind("<<ComboboxSelected>>", seleccionar_imagen)
        dropdown_contenido.pack()
        dropdown_contenido.place(x=800, y=400)

        # Crear nueva carpeta
        self.btnCrearCarpeta = tk.Button(
            self, text="Crear carpeta", command=crear_carpeta)
        self.btnCrearCarpeta.pack()
        self.btnCrearCarpeta.place(x=950, y=200)

        # Subir nuevas imagenes
        self.btnSubirImagen = tk.Button(
            self, text="Cargar imagen", command=subir_imagen)
        self.btnSubirImagen.pack()
        self.btnSubirImagen.place(x=950, y=400)

        # Reiniciar escoger
        def reset_components():
            # Clear the dropdowns
            dropdown.set("")
            dropdown_contenido.set("")

            # Clear the canvas
            if hasattr(self, "canvas_fig_agg"):
                self.canvas_fig_agg.get_tk_widget().destroy()
                del self.canvas_fig_agg
        
        self.btnReset = tk.Button(self, text="Reiniciar selección", command=reset_components)
        self.btnReset.pack()
        self.btnReset.place(x=780, y=520)

        # Seleccionar Ejes
        # self.variable =  tk.StringVar()
        # self.variable.set("Seleccionar")
        # self.labelAxis =  tk.Label(self, text ="Movimientos de ejes: ", bg="grey", fg="black" )
        # self.labelAxis.config(font=('Times new roman', 15))
        # self.labelAxis.place(x=600, y=300)
        # self.w = tk.OptionMenu(self, self.variable, 'Eje x', 'Eje y', 'Eje z')
        # self.w.place(x=800, y=300)