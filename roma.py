#coding=utf-8
import json

mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

for mese in mesi:
    print("------------------------------------------------------------")
    print("------------------------------ " + mese + " ------------------------------")
    print("------------------------------------------------------------")
    with open('./datiOriginali/Roma/'+mese+'2018.json', 'r') as jsonRoma:
        roma = json.load(jsonRoma)

    for sinistro in roma:
        print(sinistro['DataOraIncidente'] + sinistro['Strada1'])