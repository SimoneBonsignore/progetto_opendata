#coding=utf-8
#Script che fa il merge delle città in un unico csv
import csv

citta = ["Bergamo", "Matera", "Palermo", "Roma"]

#Creo il nuovo csv con tutti i dati uniti    
with open("./datiElaborati/sinistri2018.csv", "w", newline="") as sinistri2018:
    writer = csv.writer(sinistri2018, delimiter=",") 
    writer.writerow(["Citta'", "Data", "Ora", "Luogo", "Coordinate", "Illesi", "Feriti", "Riservata", "Decessi", "Natura"])
    
    for city in citta:
        print(city)
        with open("./datiElaborati/new"+city+".csv", newline="") as c:  
            lettore = csv.reader(c, delimiter=",")
            next(lettore)                                                  
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:])     