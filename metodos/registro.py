import ants
import nibabel as nib
import numpy as np

class Registro:

    def __init__(self,imagen,metodo):

        self.imagen = imagen
        self.metodo = metodo

        if metodo=="Registro":
            self.registro()
        elif metodo=="Calcular volumen":
            self.calcular_volumen()

    def registro(imagen_flair, imagen):
        # Carga las imágenes de entrada
        fixed_image = ants.image_read(imagen_flair)
        moving_image = ants.image_read(imagen)

        # Realiza el registro
        registration = ants.registration(fixed=fixed_image, moving=moving_image, type_of_transform='Rigid')

        # Obtiene la imagen registrada
        registered_image = registration['warpedmovout']

        # # Guarda la imagen registrada en el disco
        # ants.image_write(registered_image, 'ruta_de_la_imagen_registrada.nii.gz')

        # Retorna el objeto de imagen registrada
        return registered_image

    def calcular_volumen(datos_imagen):
        # Cargar los datos en una imagen Nibabel
        imagen = nib.Nifti1Image(datos_imagen, affine=None)

        # Calcular el volumen multiplicando la resolución de los pixeles por el número total de ellos
        resolucion_voxel = imagen.header['pixdim'][1:4]
        volumen = resolucion_voxel[0] * resolucion_voxel[1] * resolucion_voxel[2] * datos_imagen.size

        print("El volumen del cerebro es:", volumen)

        return volumen
