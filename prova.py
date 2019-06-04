import csv 
import re

with open("./dati/sinistri2018.csv", newline="", encoding="ISO-8859-1") as sinistri2018: #Apro il csv d'origine
    lettore = csv.reader(sinistri2018, delimiter=";") 
    header = next(lettore) 
    print(header)
    dati = [(linea[:]) for linea in lettore]
    for riga in dati:
        if riga[2]: 
            m = re.search(r"^[\sA-Z\.\']+", riga[2]).group()
            print(f"{riga[0]} " + m)
        #print(re.sub('/[^A-Z]*([A-Z]{1}[^A-Z]*[A-Z]{1}[^A-Z]*)/', '', riga[2]))


        