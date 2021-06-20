import yfinance as yf
import matplotlib.pyplot as plt
import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns #diseñado para panda
from datetime import date, timedelta
import talib as ta

# print(date.today()-2)

plt.style.use('bmh')

libname = '/Users/alvaro/Documents/TFM_Python/'

def guardar_datos(empresa):
    data = yf.download(empresa,start=date.today()-timedelta(days=730), end= date.today())
    data.to_csv(libname+empresa+'.csv',',')
    return data

def media_movil(empresa,n):
    path = '/Users/alvaro/Documents/TFM_Python/'
    data = pd.read_csv(empresa+'.csv',delimiter=',',usecols=[0,4])
    # data = data[::-1]
    data['media_movil'] = data.rolling(n).mean()
    return data['media_movil']

def fechas(empresa):
    data = pd.read_csv(empresa+'.csv',delimiter=',',usecols=[0])
    return data['Date']

# data = yf.download('AAPL','2017-1-1', date.today())

empresa__ = 'C'
# guardar_datos(empresa__)
# fechas_ = fechas(empresa__)
# media_50 = media_movil(empresa__,50)
# media_100 = media_movil(empresa__,100)
# media_200 = media_movil(empresa__,150)
# precios_ = media_movil(empresa__,1)

#!Otra forma de calcular la media movil con la libreria yfinance
data = guardar_datos(empresa__)
data['SMA_50'] = ta.SMA(data.Close.values,50)
data['SMA_100'] = ta.SMA(data.Close.values,100)
data['SMA_200'] = ta.SMA(data.Close.values,200)

#!Bandas de Bollinger con yfinance
data['upper_band'],data['middle_band'],data['lower_band'] = ta.BBANDS(data['Close'],timeperiod = 20)

#!Calculo RSI con yfinance
data['RSI'] = ta.RSI(data.Close,14)

#!Representacion gráfica
#?medias Moviles
# data[['Close','SMA_50','SMA_100','SMA_200']].plot(figsize = (15,15))
#?bandas Bollinger
# data[['Close','upper_band','middle_band','lower_band']].plot(figsize = (15,15))
#?bandas RSI
data[['Close','RSI']].plot(figsize = (15,15))
#?medias Moviles con mi metodo
# plt.plot(fechas_,media_50,fechas_,media_100,fechas_,media_200,fechas_,precios_)


#Añadimos la leyenda
# plt.legend(['media_50','media_100','media_200','precios'],loc=0)

plt.show()