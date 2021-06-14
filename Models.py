
from os import system
import csv

class Cotizaciones:

    def __init__(self, fecha, ultimo, apertura, maximo, minimo, vol):
        self.fecha = fecha
        self.ultimo = ultimo
        self.apertura = apertura
        self.maximo = maximo
        self.minimo = minimo
        self.vol = vol
        # self.diccionario_all = {}

    def __str__(self):
        print(f'''
        fecha: {self.fecha}
        ultimo: {self.ultimo}
        apertura: {self.apertura}
        maximo: {self.maximo}
        minimo: {self.minimo}
        vol: {self.vol}
        ''')
        return ''

