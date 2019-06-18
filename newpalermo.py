#coding=utf-8
#creazione di quattro csv contenenti Veicoli,Luogo,Persona,Sinistro
import csv
import datetime
ID="PA"
N=0
with open("./datiOriginali/palermo.csv", newline="",encoding="UTF-8") as P: #per ogni mese leggiamo i dati
    with open('./datiElaborati/veicoli/newPalermoVeicoli.csv','w',newline="") as newPVeicoli: #i dati sono scritti in un nuovo csv 
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPVeicoli, delimiter=",")
        writer.writerow(["ID","Modello","Targa","Tipo veicolo"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow(["ID",None,None,None]) 
            N+=1
    with open('./datiElaborati/persona/newPalermoPersona.csv','w',newline="") as newPPersona:
        P.seek(0)    #seek porta all'inizio del file aperto ogni volta che dobbiamo scrivere un nuovo csv
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPPersona, delimiter=",")
        writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow(["ID"+N,None,None,None])
    
    with open('./datiElaborati/luogo/newPalermoLuogo.csv','w',newline="") as newPLuogo:
        P.seek(0)    
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPLuogo, delimiter=",")
        writer.writerow(["ID","Citta'","Via","FondoStradale","Pavimentazione","Illuminazione"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow(["ID"+N,"Palermo",riga[2],None,None,None])

    with open('./datiElaborati/sinistro/newPalermoSinistro.csv','w',newline="") as newPSinistro:
        P.seek(0)    
        lettore = csv.reader(P, delimiter=";")
        header = next(lettore)
        writer = csv.writer(newPSinistro, delimiter=",")
        writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilità","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            writer.writerow(["ID"+N,riga[0],riga[1],None,None,None,None,None,riga[4],None,None])
                
