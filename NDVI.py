import matplotlib.pyplot as plt 
from spectral import imshow
import rasterio

b3 = rasterio.open("B3.tif")
b4 = rasterio.open("B4.tif")

B3 = b3.read(1).astype("float64")
B4 = b4.read(1).astype("float64")

ndvi = ((B4-B3)/(B4+B3))
imshow(ndvi, cmap='RdYlGn')
plt.colorbar()