from pathlib import Path
import json
import csv
import os

def cls():
    '''Limpiador de terminal'''
    os.system('cls')


def Ruta_home():
    return Path(__file__).parent.parent


def ruta_json(home):
    while True:
        if not Path(home/'data.json').exists():
            Path(home/'data.json').touch()
        else:
            return Path(home/'data.json')

'''
def save_json(ruta_j):
    while True:
        if Path(ruta_j)
''' 

def solicitar_accion():
    respuesta = input('¿Que desea hacer?:\n')
    return respuesta