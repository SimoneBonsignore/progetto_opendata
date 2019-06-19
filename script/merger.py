#coding=utf-8
#Script che fa il merge delle città in un unico csv
import csv

citta = ["Bergamo", "Matera", "Palermo", "Roma"]

#Creo il nuovo csv sinistri con tutti i dati uniti    
with open("../datiElaborati/sinistri.csv", "w", newline="") as sinistri:
    writer = csv.writer(sinistri, delimiter=",") 
    writer.writerow(["ID","Data","Ora","Tipo","Causa","Meteo","Visibilita","N.Illesi","N.Feriti","N.PrognosiRiservata","N.Deceduti"])    
    
    for city in citta:
        print(city)
        with open("../datiElaborati/sinistro/new"+city+"Sinistro.csv", newline="") as c:  
            lettore = csv.reader(c, delimiter=",")
            next(lettore)                                                  
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:])   

#Creo il nuovo csv luoghi con tutti i dati uniti    
with open("../datiElaborati/luoghi.csv", "w", newline="") as luoghi:
    writer = csv.writer(luoghi, delimiter=",") 
    writer.writerow(["ID","Citta","Via","FondoStradale","Pavimentazione","Illuminazione","Coordinate"])    
    
    for city in citta:
        print(city)
        with open("../datiElaborati/luogo/new"+city+"Luogo.csv", newline="") as c:  
            lettore = csv.reader(c, delimiter=",")
            next(lettore)                                                  
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:])

#Creo il nuovo csv veicoli con tutti i dati uniti    
with open("../datiElaborati/veicoli.csv", "w", newline="") as veicoli:
    writer = csv.writer(veicoli, delimiter=",") 
    writer.writerow(["ID","Modello","Targa","Tipo veicolo"])    
    
    for city in citta:
        print(city)
        with open("../datiElaborati/veicoli/new"+city+"Veicoli.csv", newline="") as c:  
            lettore = csv.reader(c, delimiter=",")
            next(lettore)                                                  
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:])

#Creo il nuovo csv persone con tutti i dati uniti    
with open("../datiElaborati/persone.csv", "w", newline="") as persone:
    writer = csv.writer(persone, delimiter=",") 
    writer.writerow(["ID","TipoPersona","Sesso","TipoLesione"])   
    
    for city in citta:
        print(city)
        with open("../datiElaborati/persona/new"+city+"Persona.csv", newline="") as c:  
            lettore = csv.reader(c, delimiter=",")
            next(lettore)                                                  
            dati = [(linea[:]) for linea in lettore]
            for riga in dati:
                print(f"Scrivo la riga: {riga[:]}")
                writer.writerow(riga[:]) 