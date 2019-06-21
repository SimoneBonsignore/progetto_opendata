"""
Il seguente file crea l'ontologia sulla base dei dataset creati in precedenza dagli altri script.
"""

import csv

from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF


g = Graph()

sas = Namespace("http://www.standardaccidentstructure.org/ontology/")
base_uri = "http://www.standardaccidentstructure.org/resource/"
g.bind("sas", sas)

sinistri = list()
luoghi = list()
veicoli = list()
persone = list()

personeCopia = list()

#Dataset luoghi: elaborazione e caricamento su un dizionario
print("\n\nCreo le istanze di luogo")
with open('../datiElaborati/luoghi.csv') as luogo:
        lettore = csv.DictReader(luogo)
        for riga in lettore:
                uri_luogo = base_uri + 'luogo/' + riga['ID']
                #print("\rCreo l'istanza luogo: " + uri_luogo)
                classeLuogo = sas.Luogo
                g.add([URIRef(uri_luogo), RDF.type, classeLuogo])       #Creo l'istanza della classe

                #Popolo l'istanza con gli attributi
                """
                Le URI delle citta prese in considerazione, su dbpedia sono strutturate in questo modo
                uri_palermo = "http://dbpedia.org/resource/Palermo"
                uri_roma = "http://dbpedia.org/resource/Roma"
                uri_bergamo = "http://dbpedia.org/resource/Bergamo"
                uri_matera = "http://dbpedia.org/resource/Matera"
                """
                g.add([URIRef(uri_luogo), sas.citta, URIRef("http://dbpedia.org/resource/"+riga['Citta'])])
                g.add([URIRef(uri_luogo), sas.via, Literal(riga['Via'])])
                g.add([URIRef(uri_luogo), sas.fondo_stradale, Literal(riga['FondoStradale'])])
                g.add([URIRef(uri_luogo), sas.pavimentazione, Literal(riga['Pavimentazione'])])
                g.add([URIRef(uri_luogo), sas.illuminazione, Literal(riga['Illuminazione'])])
                g.add([URIRef(uri_luogo), sas.coordinate, Literal(riga['Coordinate'])])


#Dataset veicoli: elaborazione e caricamento su un dizionario
print("Creo le istanze di veicolo")
with open('../datiElaborati/veicoli.csv') as veicolo:
        lettore = csv.DictReader(veicolo)
        count = 0 
        for riga in lettore:

                #Alcuni ID sono duplicati perche si riferiscono allo stesso sinistri quindi aggiungo un numero univoco
                uri_veicolo = base_uri + 'veicolo/' + str(count) + "-" + riga['ID']  
                count = count + 1
                #print("\rCreo l'istanza veicolo: " + uri_veicolo)
                classeVeicolo = sas.Veicolo
                g.add([URIRef(uri_veicolo), RDF.type, classeVeicolo])       #Creo l'istanza della classe

                #Popolo l'istanza con gli attributi
                g.add([URIRef(uri_veicolo), sas.modello, Literal(riga['Modello'])])
                g.add([URIRef(uri_veicolo), sas.targa, Literal(riga['Targa'])])
                g.add([URIRef(uri_veicolo), sas.tipo_veicolo, Literal(riga['Tipo veicolo'])])

#Dataset persone: elaborazione e caricamento su un dizionario
print("Creo le istanze di persona")
arrayPersona = []
with open('../datiElaborati/persone.csv') as persona:
        lettore = csv.DictReader(persona)
        count = 0 
        for riga in lettore:

                #Alcuni ID sono duplicati perche si riferiscono allo stesso sinistri quindi aggiungo un numero univoco
                uri_persona = base_uri + 'persona/' + str(count) + "-" + riga['ID']  
                count = count + 1
                #print("\rCreo l'istanza persona: " + uri_persona)
                classePersona = sas.Persona
                g.add([URIRef(uri_persona), RDF.type, classePersona])       #Creo l'istanza della classe

                #Popolo l'istanza con gli attributi
                g.add([URIRef(uri_persona), sas.tipo_persona, Literal(riga['TipoPersona'])])
                g.add([URIRef(uri_persona), sas.sesso, Literal(riga['Sesso'])])
                g.add([URIRef(uri_persona), sas.tipo_lesione, Literal(riga['TipoLesione'])])

                #Collego la persona al veicolo che stava conducendo
                uri_veicolo = base_uri + 'veicolo/' + str(count) + "-" + riga['ID']  
                g.add([URIRef(uri_persona), sas.conduce, URIRef(uri_veicolo)])

                arrayPersona.append(uri_persona)

#print(arrayPersona)

# Dataset sinistri: elaborazione e caricamento su un dizionario
print("Creo le istanze di sinistro")
with open('../datiElaborati/sinistri.csv') as sinistro:
        lettore = csv.DictReader(sinistro)
        for riga in lettore:
                uri_sinistro = base_uri + 'sinistro/' + riga['ID']
                #print("Creo l'istanza sinistro: " + uri_sinistro)
                classeSinistro = sas.Sinistro
                g.add([URIRef(uri_sinistro), RDF.type, classeSinistro])         #Creo l'istanza della classe

                #Popolo l'istanza con gli attributi
                g.add([URIRef(uri_sinistro), sas.data, Literal(riga['Data'])])
                g.add([URIRef(uri_sinistro), sas.ora, Literal(riga['Ora'])])
                g.add([URIRef(uri_sinistro), sas.tipo, Literal(riga['Tipo'])])
                g.add([URIRef(uri_sinistro), sas.causa, Literal(riga['Causa'])])
                g.add([URIRef(uri_sinistro), sas.meteo, Literal(riga['Meteo'])])
                g.add([URIRef(uri_sinistro), sas.visibilita, Literal(riga['Visibilita'])])
                g.add([URIRef(uri_sinistro), sas.illesa, Literal(riga['N.Illesi'])])
                g.add([URIRef(uri_sinistro), sas.ferita, Literal(riga['N.Feriti'])])
                g.add([URIRef(uri_sinistro), sas.prognosi_riservata, Literal(riga['N.PrognosiRiservata'])])
                g.add([URIRef(uri_sinistro), sas.deceduta, Literal(riga['N.Deceduti'])])

                #Collego il sinistro ad un luogo definito in precedenza
                uri_luogo = base_uri + 'luogo/' + riga['ID']
                g.add([URIRef(uri_sinistro), sas.localizzato, URIRef(uri_luogo)])

                #Collego il sinistro alle persone coinvolte
                for persona in arrayPersona:                       
                        if persona.split("-")[1] == riga['ID']:
                                print("##########################################################################")
                                print("Collego la persona: " + persona + " al sinistro " + riga['ID'])
                                #g.add([URIRef(uri_sinistro), sas.coinvolge, URIRef(persona['uri'])])
                                print("####################### Cancello ###############################")
                                print(persona)
                                arrayPersona.remove(persona)
                                print("####################### Array pulito ###############################")
                                print(arrayPersona)

                

"""           
#Serializzazione dell'ontologia e salvataggio
print("Serializzo l'ontologia. Attendi...")
g.serialize(destination='../standardaccidentstructure.ttl', format='turtle')
print("\nOntologia creata con SUCCESSO\n")
"""