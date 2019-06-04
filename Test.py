import csv 

with open("./dati/sinistri2018.csv", newline="", encoding="ISO-8859-1") as sinistri2018: #Apro il csv d'origine
    with open('./dati/newSinistri.csv', 'w') as newSinistri: #Creo il nuovo csv in modalità scrittura
        lettore = csv.reader(sinistri2018, delimiter=";") 
        header = next(lettore) 
        writer = csv.writer(newSinistri, delimiter=";") 
        writer.writerow(header[:]) #Copio l'header del file di origine nel nuovo file
        print(header)
        dati = [(linea[:]) for linea in lettore]
        for riga in dati:
            str = riga[0]   #Prendo solo gli elementi della colonna Data
            if "/" in str:  #Se la data contiene lo / significa che è scritta nel formato sbagliato
                print (f"{riga[0]}") #visualizzo la data nel formato errato
                #print(str[6:11]+ "-" + str[3:5] + "-" + str[0:2]) #la ristrutturo nel formato corretto
                str2 = (str[6:11] + "-" + str[3:5] + "-" + str[0:2])
                riga[0] = str2
                writer.writerow(riga[:])
            else:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:]) #In questo caso la riga è formattata come vogliamo e la copiamo nel nuovo csv

    
