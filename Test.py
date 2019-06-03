import csv 
import datetime
with open("./sinistri2018.csv", newline="", encoding="ISO-8859-1") as sinistri2018:
    with open('newSinistri.csv', 'w') as newSinistri:
        lettore = csv.reader(sinistri2018, delimiter=";") 
        header = next(lettore) 
        writer = csv.writer(newSinistri, delimiter=";") 
        writer.writerow(header[:]) #Copio l'header del file di origine nel nuovo file
        print(header)
        dati = [(linea[0], linea[1]) for linea in lettore]
        for riga in dati:
            str = riga[0]   #Prendo solo gli elementi della colonna Data
            if "/" in str:  #Se la data contiene lo / significa che è scritta nel formato sbagliato
                print (f"{riga[0]}") #visualizzo la data nel formato errato
                print(str[6:11]+ "-" + str[3:5] + "-" + str[0:2]) #la ristrutturo nel formato corretto

    
