import csv
import matplotlib.pyplot as plt
from Funciones import *  #! Aqui traes desde el archivo Leer.py, todas las funciones creadas.
import pandas as pd
from pandas import DataFrame
import numpy as np
# import datetime
import seaborn as sns #diseñado para panda


fechas_ = fechas(1)
media_50 = media_movil(50)
media_100 = media_movil(100)
media_200 = media_movil(150)
precios_ = media_movil(1)
# print(media_50)

plt.plot(fechas_,media_50,fechas_,media_100,fechas_,media_200,fechas_,precios_)
# plt.plot(fechas_,media_200,fechas_,precios_)

#Añadimos la leyenda
plt.legend(['media_50','media_100','media_200','precios'],loc=0)

plt.show()



