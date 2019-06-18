#coding=utf-8
#creazione di quattro csv contenenti Veicoli,Luogo,Persona,Sinistro
import csv
import datetime
mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre"]
corrente =0
precedente=0
for nomeMese in mesi:
    print(nomeMese)
    with open("./datiOriginali/"+nomeMese+".csv", newline="",encoding="UTF-8") as gennaio: #per ogni mese leggiamo i dati
        with open('./datiElaborati/veicoli/new'+nomeMese+'Veicoli.csv','w',newline="") as newGennaioVeicoli: #i dati sono scritti in un nuovo csv 
            lettore = csv.reader(gennaio, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newGennaioVeicoli, delimiter=",")
            writer.writerow(["ID","Modello","Targa","Tipo veicolo"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                #print(f"Scrivo la riga: {riga[0],riga[28]}")
                writer.writerow([riga[0],riga[28],None,None]) 

        with open('./datiElaborati/persona/new'+nomeMese+'Persona.csv','w',newline="") as newGennaioPersona:
            gennaio.seek(0)    #seek porta all'inizio del file aperto ogni volta che dobbiamo scrivere un nuovo csv
            lettore = csv.reader(gennaio, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newGennaioPersona, delimiter=",")
            writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                #print(f"Scrivo la riga: {riga[0],riga[28]}")
                writer.writerow([riga[0],riga[30],riga[31],riga[32]])
        
        with open('./datiElaborati/luogo/new'+nomeMese+'Luogo.csv','w',newline="") as newGennaioLuogo:
            gennaio.seek(0)    
            lettore = csv.reader(gennaio, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newGennaioLuogo, delimiter=",")
            writer.writerow(["ID","Citta'","Via","FondoStradale","Pavimentazione","Illuminazione"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                #print(f"Scrivo la riga: {riga[0],riga[28]}")
                writer.writerow([riga[0],"Roma",riga[4],riga[13],riga[14],riga[19]])

        with open('./datiElaborati/sinistro/new'+nomeMese+'Sinistro.csv','w',newline="") as newGennaioSinistro:
            gennaio.seek(0)    
            lettore = csv.reader(gennaio, delimiter=";")
            header = next(lettore)
            writer = csv.writer(newGennaioSinistro, delimiter=",")
            writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilità","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                corrente =riga[0]
                if corrente != precedente:
                    if ':'in riga[2] :
                        data = datetime.datetime.strptime(riga[2], "%d/%m/%Y %H:%M").strftime("%d-%m-%Y") #Converto la data
                        orario = datetime.datetime.strptime(riga[2], "%d/%m/%Y %H:%M").strftime("%H:%M") #Converto l'orario
                    elif "%X" in riga[2]:
                        data = datetime.datetime.strptime(riga[2], "%d/%m/%Y %H:%M:%S").strftime("%d-%m-%Y") #Converto la data
                        orario = datetime.datetime.strptime(riga[2], "%d/%m/%Y %H:%M:%S").strftime("%H:%M") #Converto l'orario
                    else:
                        data = datetime.datetime.strptime(riga[2], "%d/%m/%Y").strftime("%d-%m-%Y") #Converto la data
                        orario=None
                    writer.writerow([riga[0],"Roma",data,orario,riga[10],None,riga[16],riga[18],riga[23],riga[20],riga[21],riga[22]])
                    precedente= corrente

