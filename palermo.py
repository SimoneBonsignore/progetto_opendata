#coding=utf-8
import csv 
import re
import datetime

with open("./datiOriginali/palermo.csv", newline="", encoding="ISO-8859-1") as palermo: #Apro il csv d'origine
    with open('./datiElaborati/newPalermo.csv', 'w', newline="") as newPalermo: #Creo il nuovo csv in modalità scrittura
        lettore = csv.reader(palermo, delimiter=";") 
        header = next(lettore) 
        writer = csv.writer(newPalermo, delimiter=";") 
        writer.writerow(["Citta'", "Data", "Ora", "Luogo", "Latitudine", "Longitudine", "Illesi", "Feriti", "Riservata", "Decessi", "Natura"])
        print(header)
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            if riga[2]: #Alcune righe non hanno il Luogo e coordinate sbagliate e quindi le saltiamo
                #Assegno alla colonna Luogo solo la via senza altre informazioni
                riga[2] = re.search(r"^[\sA-Z\.\']+", riga[2]).group()

                str = riga[0]   #Prendo solo gli elementi della colonna Data
                if "/" in str:  #Se la data contiene lo / significa che è scritta nel formato sbagliato
                    riga[0] = datetime.datetime.strptime(riga[0], "%d/%m/%Y").strftime("%Y-%m-%d") #converte le date nel formato corretto

                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(["Palermo",riga[0], riga[1], riga[2], riga[5], riga[6], "", riga[4], "","",""]) #In questo caso la riga è formattata come vogliamo e la copiamo nel nuovo csv

    
