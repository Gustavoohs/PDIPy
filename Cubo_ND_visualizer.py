import spectral.io.envi as envi
from spectral import view_cube, view_nd

img = envi.open('sja_reflec_flaash.hdr', 'sja_reflec_flaash')

view_cube(img, bands=(30,60,90))

view_nd(img[:,:,:15])