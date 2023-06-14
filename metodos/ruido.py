import numpy as np

class ruido():
    def __init__(self,image,metodo):

        self.image = image
        self.metodo = metodo

        if metodo=="Filtro medio":
            self.filtro_promedio()
        elif metodo=="Filtro mediano":
            self.filtro_mediana()
    
    def filtro_promedio(imagen):
        depth, height, width = imagen.shape
        imagen_filtrada = np.zeros_like(imagen)
        for z in range(1, depth - 1):
            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    vecinos = [
                        imagen[z-1, y, x],
                        imagen[z+1, y, x],
                        imagen[z, y-1, x],
                        imagen[z, y+1, x],
                        imagen[z, y, x-1],
                        imagen[z, y, x+1],
                        imagen[z, y, x]
                    ]
                    valor_filtrado = int(np.mean(vecinos))
                    imagen_filtrada[z, y, x] = valor_filtrado

        return imagen_filtrada
    
    def filtro_mediana(imagen):
        depth, height, width = imagen.shape
        imagen_filtrada = np.zeros_like(imagen)
        for z in range(1, depth - 1):
            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    vecinos = [
                        imagen[z-1, y, x],
                        imagen[z+1, y, x],
                        imagen[z, y-1, x],
                        imagen[z, y+1, x],
                        imagen[z, y, x-1],
                        imagen[z, y, x+1],
                        imagen[z, y, x]
                    ]
                    valor_filtrado = int(np.median(vecinos))
                    imagen_filtrada[z, y, x] = valor_filtrado

        return imagen_filtrada