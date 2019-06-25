#coding=utf-8
#creazione di quattro csv contenenti Veicoli,Luogo,Persona,Sinistro
import csv
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'it_IT') #Imposto la localizzazione della data sul formato italiano

N=0

print("\n\nMatera")
with open("../datiOriginali/matera.csv", newline="",encoding="UTF-8") as M:

    print("Scrivo i veicoli")
    with open('../datiElaborati/veicolo/newMateraVeicolo.csv','w',newline="", encoding="UTF-8") as newMVeicoli: #i dati sono scritti in un nuovo csv 
        lettore = csv.reader(M, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newMVeicoli, delimiter=",")
        writer.writerow(["ID","Modello","Targa","Tipo veicolo"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            riga[4] = datetime.datetime.strptime(riga[4], "%A %d %B %Y").strftime("%Y-%m-%d") #Converto la data
            riga[5] = datetime.datetime.strptime(riga[5], "%H,%M").strftime("%H:%M") #Converto l'orario
            codice=("MT"+riga[4]+riga[5]+str(N)).replace("/", "").replace(":","").replace("-","") #unendo il codice città a N avremo un codice univoco progressivo per ogni sinistro
            writer.writerow([codice,None,None,None]) 
            N+=1
    
    print("Scrivo le persone")
    with open('../datiElaborati/persona/newMateraPersona.csv','w',newline="", encoding="UTF-8") as newMPersona:
        M.seek(0)    #seek porta all'inizio del file aperto ogni volta che dobbiamo scrivere un nuovo csv
        N=0
        lettore = csv.reader(M, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newMPersona, delimiter=",")
        writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            riga[4] = datetime.datetime.strptime(riga[4], "%A %d %B %Y").strftime("%Y-%m-%d") #Converto la data
            riga[5] = datetime.datetime.strptime(riga[5], "%H,%M").strftime("%H:%M") #Converto l'orario
            codice=("MT"+riga[4]+riga[5]+str(N)).replace("/", "").replace(":","").replace("-","")
            writer.writerow([codice,None,None,None])
            N+=1

    print("Scrivo i luoghi")    
    with open('../datiElaborati/luogo/newMateraLuogo.csv','w',newline="", encoding="UTF-8") as newMLuogo:
        M.seek(0) 
        N=0   
        lettore = csv.reader(M, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newMLuogo, delimiter=",")
        writer.writerow(["ID","Citta","Via","FondoStradale","Pavimentazione","Illuminazione","Coordinate"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            coordinate = "(" + riga[9] + "," + riga[10] + ")" #latitudine e longitudine vengono concatenate per formare un' unica variabile
            riga[4] = datetime.datetime.strptime(riga[4], "%A %d %B %Y").strftime("%Y-%m-%d") #Converto la data
            riga[5] = datetime.datetime.strptime(riga[5], "%H,%M").strftime("%H:%M") #Converto l'orario
            codice=("MT"+riga[4]+riga[5]+str(N)).replace("/", "").replace(":","").replace("-","")
            writer.writerow([codice,"Matera",riga[8],None,None,None,coordinate])
            N+=1

    print("Scrivo i sinistri")            
    with open('../datiElaborati/sinistro/newMateraSinistro.csv','w',newline="", encoding="UTF-8") as newMSinistro:
        M.seek(0) 
        N=0   
        lettore = csv.reader(M, delimiter=",")
        header = next(lettore)
        writer = csv.writer(newMSinistro, delimiter=",")
        writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilita","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            riga[4] = datetime.datetime.strptime(riga[4], "%A %d %B %Y").strftime("%Y-%m-%d") #Converto la data
            riga[5] = datetime.datetime.strptime(riga[5], "%H,%M").strftime("%H:%M") #Converto l'orario
            codice=("MT"+riga[4]+riga[5]+str(N)).replace("/", "").replace(":","").replace("-","")
            writer.writerow([codice,riga[4],riga[5],riga[12],riga[13],None,None,None,riga[17],None,riga[18]])
            N+=1
            
