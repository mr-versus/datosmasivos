# Leer el archivo csv y graficar los datos
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
data = pd.read_csv('breastcancer.csv')

# Graficar los datos de forma simple
data.plot()

# Guardar la gráfica en un archivo png
plt.savefig('breastcancer.png')
