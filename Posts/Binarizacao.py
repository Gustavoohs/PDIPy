from spectral import imshow
import skimage.io

img = skimage.io.imread('B4.tif')

mask = img < 5

imshow(mask)