#Importando bibliotecas
import matplotlib.pyplot as plt #Plotagem de gráficos
import numpy as np #Tratamento numérico (manipulação de matrizes no nosso caso)
from spectral import imshow, save_rgb #Módulo exclusivo para plotagem de imagens orbitais 
import rasterio #Tratamento de dados do tipo raster
import matplotlib.image as mpimg #Módulo para imagens (leitura, plotagem...)

#Leitura dos arquivos
b4 = rasterio.open("B4.tif")
b5 = rasterio.open("B5.tif")
b6 = rasterio.open("B6.tif")
b7 = rasterio.open("B7.tif")


#Transformação dos arquivos em arrays (Matrizes n-dimensionais)
b4 = b4.read(1).astype("float64")
b5 = b5.read(1).astype("float64")
b6 = b6.read(1).astype("float64")
b7 = b7.read(1).astype("float64")

#Armazenando todas as bandas em uma lista
lista_de_bandas1 = [b4,b5,b6,b7]

#Empilhando as bandas
stack = np.dstack(np.array(lista_de_bandas1))

fig,axes = plt.subplots(1,4,figsize=(30,13),sharex='all', sharey='all')
fig.suptitle('Bandas Separadas', fontsize=30)
axes = axes.ravel()

bandas = 4
#Plot bandas separadas
for i in range(bandas):
    axes[i].imshow(stack[:,:,i],cmap='gray')
    axes[i].set_title('Banda '+str(i+1),fontsize=25)
    axes[i].axis('off')
