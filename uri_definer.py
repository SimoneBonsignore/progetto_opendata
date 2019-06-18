import csv

from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF


g = Graph()

sas = Namespace("http://www.standartaccidentstructure.org/ontology/")
base_uri = "http://www.standartaccidentstructure.org/resource/"
g.bind("sas", sas)

geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
g.bind('geo', geo)


uri_palermo = "http://dbpedia.org/resource/Palermo"
uri_roma = "http://dbpedia.org/resource/Roma"
uri_bergamo = "http://dbpedia.org/resource/Bergamo"
uri_matera = "http://dbpedia.org/resource/Matera"

print(sas)   