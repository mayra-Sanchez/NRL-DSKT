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

        imagen_reescalada = (imagen - valor_minimo) / (valor_maximo - valor_minimo)
        return imagen_reescalada

    def z_score(imagen):
        media = imagen[imagen > 10].mean()
        desviacion_estandar = imagen[imagen > 10].std()
        imagen_zscore = (imagen - media) / desviacion_estandar 
        return imagen_zscore

    def histograma(imgOrigen, imgObjetivo):
        # Obtener los datos de las imágenes
        datos_origen = imgOrigen.get_fdata()
        datos_objetivo = imgObjetivo.get_fdata()

        # Redimensionar los datos en un solo arreglo 1D
        plano_origen = datos_origen.flatten()
        plano_objetivo = datos_objetivo.flatten()

        # Calcular los histogramas acumulativos
        hist_origen, bins = np.histogram(plano_origen, bins=256, range=(0, 255), density=True)
        hist_origen_acumulativo = hist_origen.cumsum()
        hist_objetivo, _ = np.histogram(plano_objetivo, bins=256, range=(0, 255), density=True)
        hist_objetivo_acumulativo = hist_objetivo.cumsum()

        # Ajustar los valores extremos
        valor_minimo = min(plano_origen.min(), plano_objetivo.min())
        valor_maximo = max(plano_origen.max(), plano_objetivo.max())

        # Mapear los valores de la imagen de origen a los valores de la imagen objetivo
        lut = np.interp(hist_origen_acumulativo, hist_objetivo_acumulativo, bins[:-1])

        # Aplicar el mapeo a los datos de la imagen de origen
        datos_emparejados = np.interp(datos_origen, bins[:-1], lut)

        # Ajustar los valores extremos nuevamente
        datos_emparejados = np.clip(datos_emparejados, valor_minimo, valor_maximo)

        return datos_emparejados
    
    def white_stripe(imagen):
        # Calcula el histograma
        hist, bins = np.histogram(imagen.ravel(), bins="auto")

        # Encuentra los picos del histograma
        picos, _ = find_peaks(hist)

        # Si hay al menos tres picos, utiliza el valor moda entre el segundo y el tercer pico como divisor
        if len(picos) >= 3:
            ultimo_pico = picos[-1]
            #segundo_ultimo_pico = picos[-2]
            indice_inicio = max(0, ultimo_pico - 10)
            rango_ultimo_pico = range(int(bins[indice_inicio]), int(bins[-1]) + 1)
            #rango_segundo_ultimo_pico = range(int(bins[segundo_ultimo_pico]), int(bins[ultimo_pico])+1)
            moda, _ = stats.mode(hist[rango_ultimo_pico])
            divisor = moda[0]
        # Si hay menos de tres picos, utiliza el valor moda de todo el histograma como divisor
        else:
            moda, _ = stats.mode(hist)
            divisor = moda[0]

        # Divide la imagen por el valor divisor
        #hist_normalizado = hist / divisor
        imagen_ws = imagen / divisor

        return imagen_ws