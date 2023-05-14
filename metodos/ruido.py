import numpy as np

class ruido():
    def __init__(self,image,metodo):

        self.image = image
        self.metodo = metodo

        if metodo=="Filtro medio":
            self.mean_filter()
        elif metodo=="Filtro mediano":
            self.median_filter()
    
    def mean_filter(imagen):
        depth, height, width = imagen.shape
        filtered_image = np.zeros_like(imagen)
        for z in range(1, depth - 1):
            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    neighbors = [
                        imagen[z-1, y, x],
                        imagen[z+1, y, x],
                        imagen[z, y-1, x],
                        imagen[z, y+1, x],
                        imagen[z, y, x-1],
                        imagen[z, y, x+1],
                        imagen[z, y, x]
                    ]
                    filtered_value = int(np.mean(neighbors))
                    filtered_image[z, y, x] = filtered_value

        return filtered_image
    
    def median_filter(imagen):
        depth, height, width = imagen.shape
        filtered_image = np.zeros_like(imagen)
        for z in range(1, depth - 1):
            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    neighbors = [
                        imagen[z-1, y, x],
                        imagen[z+1, y, x],
                        imagen[z, y-1, x],
                        imagen[z, y+1, x],
                        imagen[z, y, x-1],
                        imagen[z, y, x+1],
                        imagen[z, y, x]
                    ]
                    filtered_value = int(np.median(neighbors))
                    filtered_image[z, y, x] = filtered_value

        return filtered_image