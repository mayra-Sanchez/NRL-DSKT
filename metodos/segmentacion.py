import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from skimage import io

class segmentacion():
    def __init__(self,image,metodo,tau):

        self.image = image
        self.metodo = metodo
        self.tau = tau

        if metodo=="Umbralización":
            self.umbralizacion()
        elif metodo=="K-medianas":
            self.segmentacion_k_medias()
        elif metodo=="GMM":
            self.gmm()
    
    def umbralizacion(imagen,tau,tol):

        while True:
            
            segmentacion = imagen >= tau
            mBG = imagen[np.multiply(imagen > 10, segmentacion == 0)].mean()
            mFG = imagen[np.multiply(imagen > 10, segmentacion == 1)].mean()

            nuevo_tau = 0.5 * (mBG + mFG)

            if np.abs(tau - nuevo_tau) < tol:
                break
            else:
             tau = nuevo_tau
        return segmentacion

    def segmentacion_k_medias(imagen, num_clusters):
            
            num_iteraciones = 8

            # Inicialización de valores k
            valores_clusters = np.linspace(np.amin(imagen), np.amax(imagen), num_clusters)
            
            # Iteraciones del algoritmo K-medias
            for i in range(num_iteraciones):
                distancias = [np.abs(k - imagen) for k in valores_clusters]
                segmentacion = np.argmin(distancias, axis=0)

                for indice in range(num_clusters):
                    valores_clusters[indice] = np.mean(imagen[segmentacion == indice])

            return segmentacion

    def gmm(imagen):
        # Each component has a weight (wi), a mean (mui), and a standard deviation (sdi)
        w1 = 1/3
        w2 = 1/3
        w3 = 1/3
        mu1 = 0
        sd1 = 50
        mu2 = 100
        sd2 = 50
        mu3 = 150
        sd3 = 50

        seg = np.zeros_like(imagen)
        for iter in range(1, 5) :

            # Compute likelihood of belonging to a cluster
            p1 = 1/np.sqrt(2*np.pi*sd1**2) * np.exp(-0.5*np.power(imagen - mu1, 2) / sd1**2)
            p2 = 1/np.sqrt(2*np.pi*sd2**2) * np.exp(-0.5*np.power(imagen - mu2, 2) / sd2**2)
            p3 = 1/np.sqrt(2*np.pi*sd3**2) * np.exp(-0.5*np.power(imagen - mu3, 2) / sd3**2)

            # Normalise probability
            r1 = np.divide(w1 * p1, w1 * p1 + w2 * p2 + w3 * p3)
            r2 = np.divide(w2 * p2, w1 * p1 + w2 * p2 + w3 * p3) 
            r3 = np.divide(w3 * p3, w1 * p1 + w2 * p2 + w3 * p3) 

            # Update parameters
            w1 = r1.mean()
            w2 = r2.mean()
            w3 = r3.mean()
            mu1 = np.multiply(r1, imagen).sum() / r1.sum()
            sd1 = np.sqrt(np.multiply(r1, np.power(imagen - mu1, 2)).sum() / r1.sum())
            mu2 = np.multiply(r2, imagen).sum() / r2.sum()
            sd2 = np.sqrt(np.multiply(r2, np.power(imagen - mu2, 2)).sum() / r2.sum())
            mu3 = np.multiply(r3, imagen).sum() / r3.sum()
            sd3 = np.sqrt(np.multiply(r3, np.power(imagen - mu3, 2)).sum() / r3.sum())

            # Perform segmentation
            seg[np.multiply(r1 > r2, r1 > r3)] = 0
            seg[np.multiply(r2 > r1, r2 > r3)] = 1
            seg[np.multiply(r3 > r1, r3 > r2)] = 2
        
        return seg

    # def gmm(imagen, n_components):

    #     # Preprocesamiento de la imagen
    #     if len(imagen.shape) > 2:
    #         imagen = imagen[:, :, 0]

    #     # # Aplana la matriz de la imagen para obtener un vector unidimensional
    #     # data = imagen.flatten()

    #     # Normaliza los datos
    #     scaler = StandardScaler()
    #     data = scaler.fit_transform(data.reshape(-1, 1))

    #     # Crea una instancia del modelo GMM con el número de componentes deseados
    #     gmm = GaussianMixture(n_components)

    #     # Ajusta el modelo a los datos
    #     gmm.fit(data)

    #     # Obtiene las etiquetas de segmentación para cada píxel
    #     segmentation = gmm.predict(data)

    #     # Reconstruye la imagen segmentada a partir de las etiquetas
    #     segmented_image = gmm.means_[segmentation].reshape(imagen.shape)

    #     return segmented_image

