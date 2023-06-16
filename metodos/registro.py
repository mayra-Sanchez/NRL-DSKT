import ants
import nibabel as nib
import numpy as np
import os

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

        # Define the output directory path
        output_dir = "./resources/resultadosRegistros"

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Specify the output file path
        output_file = os.path.join(output_dir, "registro.nii.gz")

        # Save the registered image
        ants.image_write(registered_image, output_file)

        # Retorna el objeto de imagen registrada
        return registered_image

    def calcular_volumen(datos_imagen):
        # Crear una imagen Nibabel a partir de los datos de la imagen
        imagen = nib.Nifti1Image(np.array(datos_imagen), affine=np.eye(4))

        # Obtener la resolución de los voxels
        resolucion_voxel = imagen.header['pixdim'][1:4]

        # Calcular el volumen multiplicando la resolución de los voxels por el número total de ellos
        volumen = resolucion_voxel[0] * resolucion_voxel[1] * resolucion_voxel[2] * np.prod(datos_imagen.shape)

        print("El volumen del cerebro es:", volumen)

        return volumen
