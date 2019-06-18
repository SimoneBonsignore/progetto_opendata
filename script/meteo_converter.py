#Author: Vincenzo Guccione
#coding=utf-8

import csv
import datetime

#Creo un array che contiene i nomi dei mesi
mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

for nomeMese in mesi:
    #print(nomeMese)
    #Apro il csv d'origine
    with open("./dati/Palermo-2018-"+nomeMese+".csv", newline="", encoding="ISO-8859-1") as mese:
        #Creo il nuovo csv in modalità scrittura
        with open("./dati/2018-"+nomeMese+".csv", "w", newline="") as newMese:
            lettore = csv.reader(mese, delimiter=";") 
            header = next(lettore)
            writer = csv.writer(newMese, delimiter=";") 
            writer.writerow(header[1:2] + header[14:15]) #Copio solo le colonne che mi servono (data, fenomeno) dal header
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                fenomeno = riga[14]   #Prendo gli elementi della colonna Data
                
                if " " in fenomeno:
                    fenomeno = fenomeno[:-1]    #L'ultimo carattere nella colonna fenomeno è sempre uno spazio, lo eliminiamo
                    fenomeno = fenomeno.replace("pioggia temporale", "temporale")   #Sostituisco i fenomeni del tipo "piogga temporale" con "temporale"
                    riga[14] = fenomeno
                    #print(fenomeno)

                riga[1]=datetime.datetime.strptime(riga[1], "%d/%m/%Y").strftime("%Y-%m-%d") #Converte le date nel formato corretto
                #print(f"Scrivo la riga: {riga[1:2] + riga[14:15]}")
                writer.writerow(riga[1:2] + riga[14:15])    #Copiamo nel nuovo csv solo le colonne Data e Fenomeno

#Creo il nuovo csv con tutti i dati uniti    
with open("./dati/datiMeteo2018.csv", "w", newline="") as datiMeteo2018:
    writer = csv.writer(datiMeteo2018, delimiter=";") 
    writer.writerow(header[1:2] + header[14:15])                            #Copio solo le colonne che mi servono (data, fenomeno) dal header
    print(header[1:2] + header[14:15])
    for nomeMese in mesi:
        #print(nomeMese)
        with open("./dati/2018-"+nomeMese+".csv", newline="") as newMese:   #Apro ogni mese
            lettore = csv.reader(newMese, delimiter=";")
            next(lettore)                                                   #Salto la prima riga che contiene l'header
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:])                                        #Scrivo le restanti righe
        


           

            