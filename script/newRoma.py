#coding=utf-8
#creazione di quattro csv contenenti Veicoli,Luogo,Persona,Sinistro

import csv
import datetime
mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre"]
corrente = 0
precedente = 0

print("\n\nRoma")
for nomeMese in mesi: 
    
    if "Gennaio" in nomeMese:
        fileMode = "w"
    else:
        fileMode = "a"

    with open("../datiOriginali/"+nomeMese+".csv", newline="",encoding="UTF-8") as RM: #per ogni mese leggiamo i dati
        print("Scrivo i veicoli di " +nomeMese)
        with open('../datiElaborati/veicoli/newRomaVeicoli.csv', fileMode, newline="", encoding="UTF-8") as newRMVeicoli: #i dati sono scritti in un nuovo csv 
            lettore = csv.reader(RM, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newRMVeicoli, delimiter=",")
            writer.writerow(["ID","Modello","Targa","Tipo veicolo"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                #print(f"Scrivo la riga: {riga[0],riga[28]}")
                writer.writerow([riga[0],None,None,riga[28]]) 

        print("Scrivo le persone di " +nomeMese)
        with open('../datiElaborati/persona/newRomaPersona.csv', fileMode, newline="", encoding="UTF-8") as newRMPersona:
            RM.seek(0)    #seek porta all'inizio del file aperto ogni volta che dobbiamo scrivere un nuovo csv
            lettore = csv.reader(RM, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newRMPersona, delimiter=",")
            writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                #print(f"Scrivo la riga: {riga[0],riga[28]}")
                writer.writerow([riga[0],riga[30],riga[31],riga[32]])

        print("Scrivo i luoghi di " +nomeMese)       
        with open('../datiElaborati/luogo/newRomaLuogo.csv', fileMode, newline="", encoding="UTF-8") as newRMLuogo:
            RM.seek(0)    
            lettore = csv.reader(RM, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newRMLuogo, delimiter=",")
            writer.writerow(["ID","Citta","Via","FondoStradale","Pavimentazione","Illuminazione","Coordinate"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                corrente = riga[0] 
                if corrente != precedente:
                    coordinate = "(" + riga[24] + "," + riga[25] + ")" #latitudine e longitudine vengono concatenate
                    #print(f"Scrivo la riga: {riga[0],riga[28]}")
                    writer.writerow([riga[0],"Roma",riga[4],riga[13],riga[14],riga[19],coordinate])
                    precedente = corrente

        print("Scrivo i sinistri di " +nomeMese)           
        with open('../datiElaborati/sinistro/newRomaSinistro.csv', fileMode, newline="", encoding="UTF-8") as newRMSinistro:
            RM.seek(0)    
            lettore = csv.reader(RM, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newRMSinistro, delimiter=",")
            writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilita","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                corrente = riga[0] 
                if corrente != precedente: #confronta i numeri di protocollo in quanto ripetuti per ogni persona coinvolta
                    data_ora = riga[2].split(" ") 
                    data = datetime.datetime.strptime(data_ora[0], "%d/%m/%Y").strftime("%Y-%m-%d") #Converto la data
                    if len(data_ora) > 1:
                        orario = data_ora[1]    #Salvo l'ora se è specificata
                    else:
                        orario = None
                    
                    writer.writerow([riga[0],data,orario,riga[10],None,riga[16],riga[18],riga[23],riga[20],riga[21],riga[22]])
                    precedente = corrente


