from os import system
import csv
from Models import Cotizaciones
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd


#leemos y lo guardamos en un diccionario
def leer_():
    ruta = ''
    lectura_cotizaciones = csv.reader(open(ruta+'alibaba.csv','r'), delimiter = '|')
    for columna in lectura_cotizaciones:
        print('fecha: ',columna[0],'ultimo: ',columna[1],'apertura: ',columna[2],'maximo: ',columna[3],'minimo: ',columna[4],'vol: ',columna[5])
        coti = Cotizaciones(columna[0],columna[1],columna[2],columna[3],columna[4],columna[5])
        print(coti)

#LEEMOS EL ARCHIVO QUE YA EXISTE
def leer_2():
    libname1 = 'alibaba.csv'
    diccionario_all = {}  # EN ESTA LISTA ESTAN TODOS LOS QUE ACTUALMENTE YA EXISTEN EN EL CSV
    with open(libname1, 'r', encoding="utf-8") as archivo_actual:
        obj_csv = csv.reader(archivo_actual, delimiter="|")
        primera_fila = True
        for fila in obj_csv:
            if primera_fila:
                primera_fila = False
            else:
                diccionario_all[fila[0]] = fila
        # print(diccionario_all)
    return diccionario_all

def importar_datos(diccionario_all):
    # leer_2()
    # PATH = "C:/Program Files (x86)/chromedriver.exe" path biaggio
    PATH = "/Applications/chromedriver"
    # PATH = "/Users/alvaro/Downloads/chromedriver"

    driver = webdriver.Chrome(PATH) 
    driver.maximize_window() # Maximiza la Ventana
    driver.get("https://es.investing.com/equities/alibaba-historical-data") # Abre la dirección
    datos = driver.find_element(By.ID, 'curr_table') # aqui se busca un unico elemento

    filas = datos.find_elements(By.TAG_NAME, 'tr')[1::]

    diccionario_new = {}
    for fila in filas:
        fila = fila.text.split(" ") # print(fila.find_elements(By.TAG_NAME, 'td')[0].text,end='|') # end es para que no haga salto de linea, sino espacio 
        a = fila[0] # Fecha
        b = fila[1].replace(',','.') # Precio Ultimo
        c = fila[2].replace(',','.') # Precio Apertura
        d = fila[3].replace(',','.') # Precio Maximo
        e = fila[4].replace(',','.') # Precio Minimo
        f = fila[5].replace(',','.') # Volumen
        fila = [a, b, c, d, e, f]
        if not fila in diccionario_all.values():
            diccionario_new[a] = fila
    driver.close()

    for clave in diccionario_new.keys():
        if clave in diccionario_all.keys():
            diccionario_all.pop(clave)

    # libname = 'C:/Users/biagi/Desktop/TFM_Python/'
    libname = '/Users/alvaro/Documents/TFM_Python/' 
    fichero = 'alibaba.csv'
    csv_open = open(libname+fichero, 'w') # w es para sobrescribir, si no existe lo crea

    #! Cambié todos los "fichero.write" por "csv_open.write", ya que fichero es solo el nombre (str) del csv, y csv_open es el "fileobject".
    primera_linea = True
    for ele in diccionario_new.values():
        if primera_linea:
            csv_open.write("fecha|ultimo|apertura|maximo|minimo|vol")
            csv_open.write(f"\n{ele[0]}|{ele[1]}|{ele[2]}|{ele[3]}|{ele[4]}|{ele[5]}")
            primera_linea = False
        else:
            csv_open.write(f"\n{ele[0]}|{ele[1]}|{ele[2]}|{ele[3]}|{ele[4]}|{ele[5]}")
    for ele in diccionario_all.values():
        if primera_linea:
            csv_open.write(f"{ele[0]}|{ele[1]}|{ele[2]}|{ele[3]}|{ele[4]}|{ele[5]}")
            primera_linea = False
        else:
            csv_open.write(f"\n{ele[0]}|{ele[1]}|{ele[2]}|{ele[3]}|{ele[4]}|{ele[5]}")

    csv_open.close() #! Lo mismo, solo cambie fichero por csv_open, que es el fileobject con el que interactuamos.

def media_movil(n):
    path = '/Users/alvaro/Documents/TFM_Python/'
    data = pd.read_csv('alibaba_copy.csv',delimiter='|',usecols=[0,1])
    data = data[::-1]
    precios = pd.read_csv('alibaba_copy.csv',delimiter='|',usecols=[1])
    precios = precios[::-1]
    fechas = pd.read_csv('alibaba_copy.csv',delimiter='|',usecols=[0])
    fechas = fechas[::-1]
    data['media_movil'] = data.rolling(n).mean()
    return data['media_movil']

def fechas(n):
    path = '/Users/alvaro/Documents/TFM_Python/'
    data = pd.read_csv('alibaba_copy.csv',delimiter='|',usecols=[0,1])
    data = data[::-1]
    precios = pd.read_csv('alibaba_copy.csv',delimiter='|',usecols=[1])
    precios = precios[::-1]
    fechas = pd.read_csv('alibaba_copy.csv',delimiter='|',usecols=[0])
    fechas = fechas[::-1]
    data['media_movil'] = data.rolling(n).mean()
    return data['fecha']

# importar_datos(leer_2())
