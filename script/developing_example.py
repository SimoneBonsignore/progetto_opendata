#coding=utf-8

import csv
import datetime

corrente = 0
precedente = 0


with open("../datiOriginali/Roma/gennaio.csv", newline="", encoding="UTF-8") as roma: 
    with open('../datiElaborati/csvPerGoogle.csv', "w", newline="", encoding="UTF-8") as newRoma: 
        lettore = csv.reader(roma, delimiter=";")
        next(lettore)
        writer = csv.writer(newRoma, delimiter=",")
        writer.writerow(["ID","Via","Coordinate","Fondo Stradale","Pavimentazione","Illuminazione","Data","Ora","Tipo","Meteo","Visibilita","N. Illesi","N. Feriti","N. Prognosi Riservata","N. Deceduti"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
                corrente = riga[0] 
                if corrente != precedente:
                    
                    data_ora = riga[2].split(" ") 
                    data = data_ora[0]
                    if len(data_ora) > 1:
                        orario = data_ora[1]
                    else:
                        orario = None

                    coordinate = "(" + riga[24] + "," + riga[25] + ")"
                    writer.writerow([riga[0], riga[4], coordinate, riga[13], riga[14], riga[19], data, orario, riga[10], riga[16], riga[18], riga[23], riga[20],riga[21],riga[22]])
                    precedente = corrente

