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
        #Carga las imágenes de entrada
        fixed_image = ants.image_read(imagen_flair)
        moving_image = ants.image_read(imagen)

        #Realiza el registro
        registration = ants.registration(fixed=fixed_image, moving=moving_image, type_of_transform='SyN')

        #Obtiene la imagen registrada
        registered_image = registration['warpedmovout']

        #Guarda la imagen registrada
        salidaImagen = ants.image_write(registered_image, 'ruta_de_la_imagen_registrada.nii.gz')
        return salidaImagen


    def calcular_volumen(imagen):
        image_header = imagen.header
        pixdim = image_header['pixdim']
        pixel_size = np.prod(pixdim[1:4])

        image_data = imagen.get_fdata()
        unique_labels = np.unique(image_data.astype(int))

        cluster_volumens = {}
        for label in unique_labels:
            if label == 0:
                continue
        
            cluster_mask = (image_data == label)
            cluster_pixels = np.sum(cluster_mask)
            cluster_volumen = cluster_pixels * pixel_size

            cluster_volumens[label] = cluster_volumen
        print(cluster_volumens)
        return cluster_volumens