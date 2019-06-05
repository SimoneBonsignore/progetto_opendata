#Author: Vincenzo Guccione

import csv

#Creo un array che contiene i nomi dei mesi
mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

for nomeMese in mesi:
    print(nomeMese)
    #Apro il csv d'origine
    with open("./dati/Palermo-2018-"+nomeMese+".csv", newline="", encoding="ISO-8859-1") as mese:
        #Creo il nuovo csv in modalità scrittura
        with open("./dati/2018-"+nomeMese+".csv", "w", newline="") as newMese:
            lettore = csv.reader(mese, delimiter=";") 
            header = next(lettore)
            writer = csv.writer(newMese, delimiter=";") 
            writer.writerow(header[1:2] + header[14:15]) #Copio solo le colonne che mi servono (data, fenomeno)
            dati = [(linea[:]) for linea in lettore]
            for colonna in dati:
                fenomeno = colonna[14]   #Prendo gli elementi della colonna Data
                
                if " " in fenomeno:
                    fenomeno = fenomeno[:-1]    #L'ultimo carattere nella colonna fenomeno è sempre uno spazio, lo eliminiamo
                    fenomeno = fenomeno.replace("pioggia temporale", "temporale")   #Sostituisco i fenomeni del tipo "piogga temporale" con "temporale"
                    colonna[14] = fenomeno
                    #print(fenomeno)

                writer.writerow(colonna[1:2] + colonna[14:15]) #Copiamo nel nuovo csv solo le colonne Data e Fenomeno

