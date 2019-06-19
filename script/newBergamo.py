#coding=utf-8
#creazione di quattro csv contenenti Veicoli,Luogo,Persona,Sinistro
import csv
import datetime
N=0
with open("../datiOriginali/bergamo.csv", newline="",encoding="UTF-8") as B: #per ogni mese leggiamo i dati
    with open('../datiElaborati/veicoli/newBergamoVeicoli.csv','w',newline="") as newBVeicoli: #i dati sono scritti in un nuovo csv 
        lettore = csv.reader(B, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newBVeicoli, delimiter=",")
        writer.writerow(["ID","Modello","Targa","Tipo veicolo"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            codice="BG"+str(N)
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow([codice,None,None,None]) 
            N+=1
            
    with open('../datiElaborati/persona/newBergamoPersona.csv','w',newline="") as newBPersona:
        B.seek(0)    #seek porta all'inizio del file aperto ogni volta che dobbiamo scrivere un nuovo csv
        N=0
        lettore = csv.reader(B, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newBPersona, delimiter=",")
        writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            codice="BG"+str(N)
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow([codice,None,None,None])
            N+=1
           
    with open('../datiElaborati/luogo/newBergamoLuogo.csv','w',newline="") as newBLuogo:
        B.seek(0) 
        N=0   
        lettore = csv.reader(B, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newBLuogo, delimiter=",")
        writer.writerow(["ID","Citta","Via","FondoStradale","Pavimentazione","Illuminazione","Coordinate"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            riga[4] = riga[4].replace("BERGAMO", "")
            codice="BG"+str(N)
            #print(f"Scrivo la riga: {riga[0],riga[28]}")
            writer.writerow([codice,"Bergamo",riga[4],None,None,None,riga[14]])
            N+=1
            
    with open('../datiElaborati/sinistro/newBergamoSinistro.csv','w',newline="") as newBSinistro:
        B.seek(0) 
        N=0   
        lettore = csv.reader(B, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newBSinistro, delimiter=",")
        writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilita","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            riga[2]=datetime.datetime.strptime(riga[2], "%d/%m/%Y").strftime("%Y-%m-%d") #Converte le date nel formato corretto
            codice="BG"+str(N)
            writer.writerow([codice,riga[2],riga[3],None,None,None,None,riga[6],riga[7],riga[8],riga[9]])
            N+=1