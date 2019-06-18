#coding=utf-8
#creazione di quattro csv contenenti Veicoli,Luogo,Persona,Sinistro
import csv
import datetime
N=0
with open("../datiOriginali/palermo.csv", newline="",encoding="UTF-8") as P: #per ogni mese leggiamo i dati
    with open('./datiElaborati/veicoli/newPalermoVeicoli.csv','w',newline="") as newPVeicoli: #i dati sono scritti in un nuovo csv 
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPVeicoli, delimiter=",")
        writer.writerow(["ID","Modello","Targa","Tipo veicolo"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            codice="PA"+str(N)
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow([codice,None,None,None]) 
            N+=1
            
    with open('../datiElaborati/persona/newPalermoPersona.csv','w',newline="") as newPPersona:
        P.seek(0)    #seek porta all'inizio del file aperto ogni volta che dobbiamo scrivere un nuovo csv
        N=0
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPPersona, delimiter=",")
        writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            codice="PA"+str(N)
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow([codice,None,None,None])
            N+=1
           
    with open('../datiElaborati/luogo/newPalermoLuogo.csv','w',newline="") as newPLuogo:
        P.seek(0) 
        N=0   
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPLuogo, delimiter=",")
        writer.writerow(["ID","Citta'","Via","FondoStradale","Pavimentazione","Illuminazione","Coordinate"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            coordinate = "(" + riga[6] + "," + riga[5] + ")"
            codice="PA"+str(N)
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow([codice,"Palermo",riga[2],None,None,None,coordinate])
            N+=1
            
    with open('../datiElaborati/sinistro/newPalermoSinistro.csv','w',newline="") as newPSinistro:
        P.seek(0) 
        N=0   
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPSinistro, delimiter=",")
        writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilita","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            codice="PA"+str(N)
            writer.writerow([codice,riga[0],riga[1],None,None,None,None,None,riga[4],None,None])
            N+=1
            