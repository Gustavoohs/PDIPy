from spectral import *
import numpy as np
import pylab as plt

# Criando o banco de dados e copiando os arquivos ECOSTRESS para ele
db = EcostressDatabase.create('ecostress.db', 
                                  'C:/Users/Pichau/ecospeclib-all')

# Acessando o banco
db = EcostressDatabase('ecostress.db')

# Realizando consultas
db.print_query('SELECT COUNT() FROM Samples WHERE Name LIKE "%kaolinite%"')
db.print_query('SELECT SampleID, Name FROM Samples WHERE Name LIKE "%kaolinite%" limit 5')

# Visualizando espectro da Caulinita
f = plt.figure()
s = db.get_signature(966)
plt.plot(s.x, s.y)

# Lendo arquivo de calibração de bandas AVIRIS
bands = aviris.read_aviris_bands('92AV3C.spc')

# Verificando as unidades dos espectrtos de caulinita
db.print_query('SELECT DISTINCT Measurement, XUnit, YUnit FROM Samples, Spectra ' +
               'WHERE Samples.SampleID = Spectra.SampleID AND ' +
               'Name LIKE "%kaolinite%"')

# Consultando os espectros de caulinita nos limites das bandas do AVIRIS
db.print_query('SELECT COUNT() FROM Samples, Spectra ' +
               'WHERE Samples.SampleID = Spectra.SampleID AND ' +
               'Name LIKE "%kaolinite%" AND ' +
               'MinWavelength <= 0.4 AND MaxWavelength >= 2.5')


# Selecionando os espectros de caulinita para reamostrar
rows = db.query('SELECT SpectrumID FROM Samples, Spectra ' +
                'WHERE Samples.SampleID = Spectra.SampleID AND ' +
                'Name LIKE "%kaolinite%" AND ' +
                'MinWavelength <= 0.4 AND MaxWavelength >= 2.5')

# IDs dos espectros
ids = [r[0] for r in rows]

# Convertendo unidades (de nanômetros para micrômetros)
bands.centers = [x / 1000. for x in bands.centers]
bands.bandwidths = [x / 1000. for x in bands.bandwidths]

# Criando biblioteca de caulinita
lib = db.create_envi_spectral_library(ids, bands)

# Visualizando resultado da reamostragem
figu = plt.figure()
spec = db.get_signature(ids[-1])
plt.plot(spec.x, spec.y, 'k-', label='original')
plt.plot(bands.centers, lib.spectra[-1], 'r-', label='reamostrado')
plt.grid(1)
plt.gca().legend(loc='upper left')
plt.xlim(0, 3)
plt.title('Espectro reamostrado de Caulinita' % lib.names[-1])

