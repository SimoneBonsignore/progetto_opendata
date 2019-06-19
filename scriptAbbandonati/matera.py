#coding=utf-8
#Script che estrae i dati contenuti nel file matera.csv
#Author: Vincenzo Guccione

import csv 
import re
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'it_IT') #Imposto la localizzazione della data sul formato italiano

with open("../datiOriginali/matera.csv", newline="", encoding="UTF-8") as matera: #Apro il csv d'origine
    with open('../datiElaborati/newMatera.csv', 'w', newline="") as newMatera: #Creo il nuovo csv in modalità scrittura
        lettore = csv.reader(matera, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newMatera, delimiter=",")
        writer.writerow(["Citta'", "Data", "Ora", "Luogo", "Coordinate", "Illesi", "Feriti", "Riservata", "Decessi", "Tipo","Causa","Visibilità","Fondo_stradale","Meteo","Pavimentazione","Illuminazione"])
        #print(header)
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            riga[0] = "Matera"
            riga[6] = 0
            riga[4] = datetime.datetime.strptime(riga[4], "%A %d %B %Y").strftime("%Y-%m-%d") #Converto la data
            riga[5] = datetime.datetime.strptime(riga[5], "%H,%M").strftime("%H:%M") #Converto l'orario
            coordinate = "(" + riga[9] + "," + riga[10] + ")"
            print(f"Scrivo la riga: Matera { riga[4] + riga[5] + riga[8] + coordinate} 0 { riga[17]} 0 { riga[18] + riga[12]}")
            writer.writerow(["Matera" , riga[4] , riga[5] , riga[8] , coordinate , "0" , riga[17] , "0" , riga[18] , riga[12],riga[13],None, None, None, None, None])
