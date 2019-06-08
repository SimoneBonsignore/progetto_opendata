#coding=utf-8
#Script che estrae i dati contenuti nei file JSON riguardanti i sinistri a Roma
import json
import csv
import datetime

mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre"]
citta = "Roma"

with open("./datiElaborati/newRoma.csv", "w", newline="", encoding="UTF-8") as newRoma:
    writer = csv.writer(newRoma, delimiter=";")
    writer.writerow(["Citta'", "Data", "Ora", "Luogo", "Latitudine", "Longitudine", "Illesi", "Feriti", "Riservata", "Decessi", "Natura"])
    
    for mese in mesi:
        print("------------------------------------------------------------")
        print("------------------------ " + mese + " ----------------------")
        print("------------------------------------------------------------")
        with open('./datiOriginali/Roma/'+mese+'2018.json', 'r') as jsonRoma:
            roma = json.load(jsonRoma)
            for sinistro in roma:
                if sinistro['Latitudine'] != None and sinistro['Longitudine'] != None:
                    data_ora = sinistro['DataOraIncidente'].split(" ")
                    data_ora[1] = datetime.datetime.strptime(data_ora[1], "%H:%M:%S.%f").strftime("%H:%M")

                    print("Scrivo la riga: " + citta + " " + data_ora[0] + " " + data_ora[1] + " " + sinistro['Strada1'] + " " + sinistro['Latitudine'] + " " + sinistro['Longitudine'] + " " + sinistro['NUM_ILLESI'] + " " + sinistro['NUM_FERITI'] + " " + sinistro['NUM_RISERVATA'] + " " + sinistro['NUM_MORTI'] + " " + sinistro['NaturaIncidente'])
                    writer.writerow([citta , data_ora[0] , data_ora[1] , sinistro['Strada1'] , sinistro['Latitudine'] , sinistro['Longitudine'] , sinistro['NUM_ILLESI'] , sinistro['NUM_FERITI'] , sinistro['NUM_RISERVATA'] , sinistro['NUM_MORTI'] , sinistro['NaturaIncidente']])
