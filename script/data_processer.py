import csv

from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF


g = Graph()

sas = Namespace("http://www.standardaccidentstructure.org/ontology/")
base_uri = "http://www.standardaccidentstructure.org/resource/"
g.bind("sas", sas)

geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
g.bind('geo', geo)


uri_palermo = "http://dbpedia.org/resource/Palermo"
uri_roma = "http://dbpedia.org/resource/Roma"
uri_bergamo = "http://dbpedia.org/resource/Bergamo"
uri_matera = "http://dbpedia.org/resource/Matera"

sinistri = list()

# Dataset sinistri Roma: elaborazione e caricamento su un dizionario
with open('../datiElaborati/sinistro/newGennaioSinistro.csv') as sinistro:
    lettore = csv.DictReader(sinistro)
    for riga in lettore:
        uri_sinistro = base_uri + 'sinistro/' + riga['ID']
        print("Creo l'istanza: " + uri_sinistro)
        classeSinistro = sas.Sinistro
        g.add([URIRef(uri_sinistro), RDF.type, classeSinistro])

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

        sinistro = dict()
        sinistro['uri'] = uri_sinistro
        sinistri.append(sinistro)



"""
        g.add([URIRef(uri_parafarmacia), RDF.type, classeParafarmacia])
        g.add([URIRef(uri_parafarmacia), ppa.denominazione, Literal(row['DENOMINAZIONESITO'])])

        posizioneGPS = BNode()
        g.add([posizioneGPS, RDF.type, URIRef(geo.point)])
        g.add([posizioneGPS, geo.lat, Literal(row['LAT'])])
        g.add([posizioneGPS, geo.long, Literal(row['LNG'])])
        g.add([URIRef(uri_parafarmacia), ppa.posizioneGPS, posizioneGPS])

        g.add([URIRef(uri_parafarmacia), ppa.indirizzo, Literal(row['INDIRIZZO'])])
        g.add([URIRef(uri_parafarmacia), ppa.CAP, Literal(row['CAP'])])
        g.add([URIRef(uri_parafarmacia), ppa.citta, URIRef(uri_palermo)])

        dataUltimoAggiornamento = row['ULTIMOAGGIORNAMENTO']+'-01'
        g.add([URIRef(uri_parafarmacia), ppa.ultimoAggiornamento, Literal(dataUltimoAggiornamento)])


        parafarmacia = dict()
        parafarmacia['uri'] = uri_parafarmacia
        parafarmacia['lat'] = row['LAT']
        parafarmacia['long'] = row['LNG']
        parafarmacie.append(parafarmacia)
        """
g.serialize(destination='../standardaccidentstructure.ttl', format='turtle')