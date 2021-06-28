#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:15:01 2021

@author: Gustavo Ferreira
"""
#---------------------------------------------------------------------------------------------------
#Importação das bibliotecas
from scipy.misc import imsave
import matplotlib.pyplot as plt
import numpy as np
from spectral import imshow, save_rgb
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio
from rasterio import plot
from rasterio.plot import show_hist

#---------------------------------------------------------------------------------------------------
#Leitura dos arquivos

b4 = rasterio.open("/home/gustavo/Área de trabalho/rasters/B4.tif")
b5 = rasterio.open("/home/gustavo/Área de trabalho/rasters/B5.tif")
b6 = rasterio.open("/home/gustavo/Área de trabalho/rasters/B6.tif")
b7 = rasterio.open("/home/gustavo/Área de trabalho/rasters/B7.tif")


#Transformação dos arquivos em arrays (Matrizes n-dimensionais)
b4 = b4.read(1).astype("float64")
b5 = b5.read(1).astype("float64")
b6 = b6.read(1).astype("float64")
b7 = b7.read(1).astype("float64")


#Armazenando todas as bandas em ma lista
lista_de_bandas1 = [b4,b5,b6,b7]
#---------------------------------------------------------------------------------------------------

banda4 = "/home/gustavo/Área de trabalho/rasters/B4.tif"
banda5 = "/home/gustavo/Área de trabalho/rasters/B5.tif"
banda6 = "/home/gustavo/Área de trabalho/rasters/B6.tif"
banda7 = "/home/gustavo/Área de trabalho/rasters/B7.tif"


lista_de_bandas2 = [banda4,banda5,banda6,banda7]
#---------------------------------------------------------------------------------------------------
#Empilhamento das imagens

stack = np.dstack(np.array(lista_de_bandas1))
stack2, meta_data = es.stack(lista_de_bandas2)
#---------------------------------------------------------------------------------------------------


#Parâmetros de plotagem
titles = ["Green", "Red", "NIR 1", "NIR 2"]

colors_list = [
        
    "Green",
    "Red",
    "Maroon",
    "Purple",
]
x_axis = [ 0.55, 0.65, 0.75, 0.95 ]

#b3[b3 == 0] = np.nan

#ep.hist(stack2, bins = 200, colors=colors_list, title=titles)
#plt.show()

#ep.hist(b3, bins=50, cols=3)
#plt.show()

#ep.plot_bands(stack2, title=titles)
#plt.show()

#imshow(stack, stretch=(0.02, 0.98))

#---------------------------------------------------------------------------------------------------
#NDVI

ndvi = ((b6-b5)/(b6+b5))
imshow(np.array(ndvi), cmap="brg")
plt.colorbar() 

#---------------------------------------------------------------------------------------------------
#Salvar imagens no disco

#save_rgb('rgb.jpg', stack, [2, 3, 4])

#imsave("image.tif", stack)

#---------------------------------------------------------------------------------------------------
fig1, ax = plt.subplots()

ax.plot(x_axis,stack[294,416], color = 'green')

ax.set(xlabel='Wavelength')
ax.grid()

#fig1.savefig("espectro.png", dpi=300)
plt.show()
