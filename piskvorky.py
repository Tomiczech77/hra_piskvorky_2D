from util import tah
from ai import tah_pocitace

def vyhodnot(herni_pole):
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    else:
        return "-"

def tah_hrace(herni_pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole"""
    while True:
        pozice = input("Kam chceš hrát? ").strip()
        try:
            pozice = int(pozice)
        except ValueError:
            print("Zadávej jen číslo!")
            continue
        try:
            return tah(herni_pole, pozice, symbol)
        except ValueError as chyba:
            print(chyba)

def piskvorky1d():
    herni_pole = 20 * "-"
    pocet_kol = 1
    while True:
        herni_pole = tah_hrace(herni_pole, "x")
        print(f"{pocet_kol}. kolo: {herni_pole}")
        if vyhodnot(herni_pole) != "-":
            break
        pocet_kol += 1
        herni_pole = tah_pocitace(herni_pole, "o")
        print(f"{pocet_kol}. kolo: {herni_pole}")
        if vyhodnot(herni_pole) != "-":
            break
        pocet_kol += 1
    if vyhodnot(herni_pole) == "x":
        print("Gratuluji, výhra je Tvoje!")
    elif vyhodnot(herni_pole) == "o":
        print("Prohra, počítač byl lepší...")
    elif vyhodnot(herni_pole) == "!":
        print("Remíza!")