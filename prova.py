#Author: Vincenzo Guccione

import csv

#Creo un array che contiene i nomi dei mesi
mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
headers = ["Data", "Fenomeni"]

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
            for riga in dati:
                fenomeno = riga[14]   #Prendo solo gli elementi della colonna Data
                #print(fenomeno)
                
                if " " in fenomeno:
                    #fenomeno = fenomeno.replace(" ", "_")
                    print(fenomeno[-1])
                #if "/" in str:  #Se la data contiene lo / significa che è scritta nel formato sbagliato
                    #print (f"{riga[0]}") #visualizzo la data nel formato errato
                    #print(str[6:11]+ "-" + str[3:5] + "-" + str[0:2]) #la ristrutturo nel formato corretto
                    #print(riga[1])
                    #print(str[6:11] + "-" + str[3:5] + "-" + str[0:2])
                    #print(str[6:11])
                    #print(str[3:5])
                    #print(str[0:2])
                    #newData = (str[6:11] + "-" + str[3:5] + "-" + str[0:2])
                    #riga[1] = newData
                    #print(riga[1])
                    #writer.writerow(riga[:]) #In questo caso la riga è formattata come vogliamo e la copiamo nel nuovo csv

