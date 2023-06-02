import numpy as np
from scipy.signal import find_peaks
import scipy.stats as stats

class intensidad():
    def __init__(self,image,metodo):

        self.image = image
        self.metodo = metodo

        if metodo=="Reescala":
            self.reescala()
        elif metodo=="z-score":
            self.z_score()
        elif metodo=="Coincidencia de histograma":
            self.histograma()
        elif metodo=="Raya blanca":
            self.white_stripe()
    
    def reescala(imagen):
        valor_minimo = imagen.min()
        valor_maximo = imagen.max()

        image_data_rescaled = (imagen - valor_minimo) / (valor_maximo - valor_minimo)
        return image_data_rescaled

    def z_score(imagen):
        mean = imagen[imagen > 10].mean()
        standard_deviation = imagen[imagen > 10].std()
        image_zscore = (imagen - mean)/(standard_deviation) 
        return image_zscore

    def histograma():
        pass
    
    def white_stripe(imagen):
        # Calcula el histograma
        hist, bins = np.histogram(imagen.ravel(), bins="auto")

        # Encuentra los picos del histograma
        peaks, _ = find_peaks(hist)

        # Si hay al menos tres picos, utiliza el valor moda entre el segundo y el tercer pico como divisor
        if len(peaks) >= 3:
            last_peak = peaks[-1]
            #second_last_peak = peaks[-2]
            start_index = max(0, last_peak - 10)
            last_peak_range = range(int(bins[start_index]), int(bins[-1]) + 1)
            #second_last_peak_range = range(int(bins[second_last_peak]), int(bins[last_peak])+1)
            mode, _ = stats.mode(hist[last_peak_range])
            divisor = mode[0]
        # Si hay menos de tres picos, utiliza el valor moda de todo el histograma como divisor
        else:
            mode, _ = stats.mode(hist)
            divisor = mode[0]

        # Divide el histograma por el valor divisor
        #hist_norm = hist / divisor
        image_ws = imagen / divisor

        return image_ws