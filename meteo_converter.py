#Author: Vincenzo Guccione

import csv

#Creo un array che contiene i nomi dei mesi
mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

for nomeMese in mesi:
    print(nomeMese)
    #Apro il csv d'origine
    with open("./dati/Palermo-2018-"+nomeMese+".csv", newline="", encoding="ISO-8859-1") as mese:
        #Creo il nuovo csv in modalità scrittura
        with open("./dati/2018-"+nomeMese+".csv", "w") as newMese:
            lettore = csv.reader(mese, delimiter=";") 
            header = next(lettore)
            writer = csv.writer(newMese, delimiter=";") 
            writer.writerow(header[:]) #Copio l'header del file di origine nel nuovo file

