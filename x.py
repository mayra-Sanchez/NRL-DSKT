import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import Tk, Label, Button,filedialog
import nibabel as nib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from metodos.segmentacion import segmentacion

class ventanaSubirImagen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Subir imagen")
        self.config(bg="grey")
        self.geometry("1200x610")

        # Definir los componentes de la nueva ventana
        self.etiqueta = Label(self, text="NRL-DSKT")
        self.etiqueta.pack()
        self.etiqueta.config(font=('Times new roman', 35))
        self.etiqueta.place(x=100, y=30)
        self.etiqueta.config(bg="grey")

        self.botonCargar = Button(self, text="Cargar imagen", command=self.cargar_imagen)
        self.botonCargar.pack()
        self.botonCargar.place(x=280, y=570)

        # Crear un lienzo para mostrar la imagen
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.place(x=100, y= 100, width=450, height=450)

        # Seleccionar Ejes
        self.variable =  tk.StringVar()
        self.variable.set("Seleccionar")
        self.labelAxis =  tk.Label(self, text ="Movimientos de ejes: ",bg="grey", fg="black" )
        self.labelAxis.place(x=580, y= 100)
        self.w =  tk.OptionMenu(self, self.variable, 'Eje x','Eje y','Eje z',command=self.ejes)
        self.w.place(x=700, y= 100)

        # Seleccionar Segmentacion
        self.segmentacion_m =  tk.StringVar()
        self.segmentacion_m.set("Seleccionar") 
        self.labelMethod1 =  tk.Label(self, text ="Segmentación: ", bg="grey",fg="black" )
        self.labelMethod1.place(x=580, y= 180 )
       
        self.opc1 =  tk.OptionMenu(self, self.segmentacion_m, "Umbralización","K-medianas", "GMM", command=self.seleccion_segmentacion)
        self.opc1.place(x=700, y= 180)

        # Seleccionar Intensidad
        self.intensidad_m =  tk.StringVar()
        self.intensidad_m.set("Seleccionar") 
        self.labelMethod2 =  tk.Label(self, text ="Intensidad: ", bg="grey",fg="white" )
        self.labelMethod2.place(x=10, y= 255, width=450,height=50)
       
        self.opc2 =  tk.OptionMenu(self, self.intensidad_m, "Reescala","z-score", "Coincidencia de histograma", "Raya blanca", command=self.display_selected)
        self.opc2.place(x=480, y= 260, width=150,height=40)

        # Seleccionar Ruido
        self.ruido_m =  tk.StringVar()
        self.ruido_m.set("Seleccionar") 
        self.labelMethod3 =  tk.Label(self, text ="Ruido: ", bg="grey",fg="white" )
        self.labelMethod3.place(x=10, y= 255, width=450,height=50)
       
        self.opc3 =  tk.OptionMenu(self, self.ruido_m,  "Filtro medio", "Filtro mediano", command=self.display_selected)
        self.opc3.place(x=480, y= 260, width=150,height=40)

    def cargar_imagen(self):
        self.file_path = filedialog.askopenfilename()
        self.rutaImage=self.file_path
        self.img = nib.load(self.rutaImage)
        self.imagen = self.img.get_fdata()
        self.iniciar()
        
    def click(self,event):
        if self.ax.contains(event)[0]:
            x = int(event.xdata)
            y = int(event.ydata)

    def iniciar(self):
        self.canvas.delete("all")
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.imagen[:,:,5])
        self.canvas_widget = FigureCanvasTkAgg(self.fig, self.canvas)
        self.canvas_widget.draw()
        self.canvas_widget.get_tk_widget().place( x=0, y=0,width=450, height=450)
        cid = self.fig.canvas.mpl_connect('button_press_event', self.click)
    
    def escala(self,*args):
            
        if self.rutaImage!="":
            self.canvas.delete("all")
            if self.variable.get()=='Eje x':
                self.ax.imshow(self.imagen[self.escalaEjes.get(),:,:])
            elif self.variable.get()=='Eje y':
                self.ax.imshow(self.imagen[:,self.escalaEjes.get(),:])
            elif self.variable.get()=='Eje z':
                self.ax.imshow(self.imagen[:,:,self.escalaEjes.get()])
            else:
                self.ax.imshow(self.imagen[:,:,5])
            self.canvas_widget.draw()
        else:
            pass
           
    def ejes(self, *args):
        if self.variable.get()=='X' and self.rutaImage!="" :
            self.size = (self.imagen.shape[0])-1
        elif self.variable.get()=='Y' and self.rutaImage!="" :
            self.size = (self.imagen.shape[1])-1
        elif self.variable.get()=='Z' and self.rutaImage!="":
            self.size = (self.imagen.shape[2])-1
        else:
            self.size=10
        self.escalaEjes = tk.Scale(self, label=self.variable.get(),from_=0, to=self.size, orient='vertical', bg="grey",fg="black",command=self.escala)
        self.escalaEjes.place(x=20, y= 100)

    def seleccion_segmentacion(self, *args):
        canvasSegmentacion = tk.Canvas(self, width=300, height=200, bg="grey", highlightbackground="grey", highlightthickness=2)
        canvasSegmentacion.pack()
        canvasSegmentacion.place(x= 850, y= 100)
        if self.segmentacion_m.get()=='Umbralización' and self.rutaImage!="" :
            self.tautext = tk.Label(canvasSegmentacion, text ="Tau:", bg="grey",fg="black" )
            self.tautext.place(x=100, y= 10)
            self.Tau = tk.Entry(canvasSegmentacion,justify="center")
            self.Tau.insert(0, "110")
            self.Tau.place(x=100, y= 50)

            self.toletext = tk.Label(canvasSegmentacion, text ="Tolerancia:", bg="grey",fg="black" )
            self.toletext.place(x=100, y= 90)
            self.Tol = tk.Entry(canvasSegmentacion,justify="center")
            self.Tol.insert(0, "1")
            self.Tol.place(x=100, y=130)

            self.btn = tk.Button(canvasSegmentacion, text="Aceptar", bg="white", borderwidth=0, command= lambda: self.confirmacion("1"))
            self.btn.place(x=130, y= 160)

        if self.segmentacion_m.get()=='K-medianas' and self.rutaImage!="" :
            self.ks = tk.Label(canvasSegmentacion, text ="Cantidad de clusters:", bg="grey",fg="black" )
            self.ks.place(x=100, y= 50)
            self.clusters = tk.Entry(canvasSegmentacion,justify="center")
            self.clusters.insert(0, "2")
            self.clusters.place(x=100, y=90)

            self.btn = tk.Button(canvasSegmentacion, text="Aceptar", bg="white", borderwidth=0, command= lambda: self.confirmacion("2"))
            self.btn.place(x=150, y= 160)
        if self.segmentacion_m.get()=='GMM' and self.rutaImage!="" :
            # self.componentes = tk.Label(canvasSegmentacion, text ="Numero de componentes:", bg="grey",fg="black" )
            # self.componentes.place(x=100, y= 50)
            # self.num_componentes = tk.Entry(canvasSegmentacion,justify="center")
            # self.num_componentes.insert(0, "3")
            # self.num_componentes.place(x=100, y=90)

            # self.btn = tk.Button(canvasSegmentacion, text="Aceptar", bg="white", borderwidth=0, command= lambda: self.confirmacion("3"))
            # self.btn.place(x=150, y= 160)
            self.imagen = self.img.get_fdata()
            self.imagen=segmentacion.gmm(self.imagen)
            self.escala()

    def seleccion_intensidad(self, *args):
        if self.intensidad_m.get()=='Reescala' and self.rutaImage!="" :
            pass
        if self.intensidad_m.get()=='z-score' and self.rutaImage!="" :
            pass
        if self.intensidad_m.get()=='Coincidencia de histograma' and self.rutaImage!="" :
            pass
        if self.intensidad_m.get()=='Raya blanca' and self.rutaImage!="" :
            pass

    def seleccion_ruido(self, *args):
        if self.ruido_m.get()=='Filtro medio' and self.rutaImage!="" :
            pass
        if self.ruido_m.get()=='Filtro mediano' and self.rutaImage!="" :
            pass
   

    def confirmacion(self,metodo):
        if metodo=="1":
            self.imagen = self.img.get_fdata()
            self.imagen=segmentacion.umbralizacion(self.imagen, int(self.Tau.get()), int(self.Tol.get()))
            self.escala()
        elif metodo=="2":
            self.imagen = self.img.get_fdata()
            self.imagen=segmentacion.segmentacion_k_medias(self.imagen, int(self.clusters.get()))
            self.escala()
        # elif metodo=="3":
        #     self.imagen = self.img.get_fdata()
        #     self.imagen=segmentacion.gmm(self.imagen,int(self.num_componentes.get()))
        #     self.escala()
