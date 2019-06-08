#author Simone Bonsignore
#coding=utf-8
import csv 
import datetime

with open("./datiOriginali/bergamo.csv", newline="", encoding="UTF-8") as bergamo: #Apro il csv d'origine
    with open('./datiElaborati/newBergamo.csv', 'w', newline="",encoding ="UTF-8") as newBergamo: #Creo il nuovo csv in modalità scrittura
        lettore =csv.reader(bergamo,delimiter=",")
        header= next(lettore)
        writer= csv.writer(newBergamo,delimiter=";")
        writer.writerow(["Citta'", "Data", "Ora", "Luogo", "Coordinate", "Illesi", "Feriti", "Riservata", "Decessi", "Natura"])        
        print(header)
        dati=[(linea[:]) for linea in lettore]
        for riga in dati:
            if '2017' in riga[1]:
                riga[4] = riga[4].replace("BERGAMO", "")
                #riga[14] = riga[14].replace("(","").replace(")","")
                #coord=riga[14].split(",") #creo una variabile coordinate che tiene conto del separatore
                #print (coord)
                riga[2]=datetime.datetime.strptime(riga[2], "%d/%m/%Y").strftime("%Y-%m-%d") #Converte le date nel formato corretto
                #print(f"Scrivo la riga: {riga[:]}") 
                #writer.writerow(riga[:]) #In questo caso la riga è formattata come vogliamo e la copiamo nel nuovo csv
                writer.writerow(["Bergamo", riga[2] , riga[3] , riga[4] , riga[14],  riga[6] , riga[7] , riga[8], riga[9],riga[5]])    #Copiamo nel nuovo csv solo le colonne che ci servono, coord 0 e coord 1 sono le coordinate prese singolarmente