def tah(herni_pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    if pozice < 0 or pozice > 19:
        raise ValueError ("Pozice musí být od 0 do 19.")
    elif herni_pole[pozice] != "-":
        raise ValueError ("Pozice je obsazená.")
    elif symbol != "x" and symbol != "o":
        raise ValueError ('Použij pouze "x" nebo "o".')
    zacatek_pole = herni_pole[:pozice]
    konec_pole = herni_pole[pozice + 1:]
    herni_pole = zacatek_pole + symbol + konec_pole
    return herni_pole