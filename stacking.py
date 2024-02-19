#Importação das bibliotecas
import numpy as np
import rasterio


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


#Armazenando todas as bandas em ma lista
lista_de_bandas1 = [b4,b5,b6,b7]

#Empilhamento das imagens

stack = np.dstack(np.array(lista_de_bandas1))