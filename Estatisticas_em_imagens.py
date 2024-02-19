import numpy as np
from osgeo import gdal

b2 = gdal.Open('B2.tif')
b3 = gdal.Open('B3.tif')
b4 = gdal.Open('B4.tif')
b5 = gdal.Open('B5.tif')

B2 = b2.ReadAsArray()
B3 = b3.ReadAsArray()
B4 = b4.ReadAsArray()
B5 = b5.ReadAsArray()

lista_de_bandas = [B2,B3,B4,B5]

media=[]
var=[]
std=[]

for i in lista_de_bandas:
	media.append(np.mean(i))
	var.append(np.var(i))
	std.append(np.std(i))

print(media)
print(var)
print(std)