from random import randrange
from util import tah

def tah_pocitace(herni_pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače"""
    while True:
        pozice = randrange(20)
        if herni_pole[pozice] == "-":
            return tah(herni_pole, pozice, symbol)