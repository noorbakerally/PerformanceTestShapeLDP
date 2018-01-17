# coding=utf-8
from rdflib import Graph
import random

top = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/api/v2/catalog/exports/ttl> a dcat:Catalog ;
    dct:Language <http://id.loc.gov/vocabulary/iso639-1/en>,
        <http://id.loc.gov/vocabulary/iso639-1/fr> ;
    dct:description "Bistrotdepays Catalog" ;
    dct:publisher <http://www.opendatasoft.com> ;
    dct:title "Bistrotdepays's catalog" . """

placeHolder = """<https://example.com/api/v2/catalog/exports/ttl> dcat:dataset <https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays> .

<https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays> a dcat:Dataset ;
    dct:description "Liste des animations dans les établissements du label Bistrot de Pays." ;
    dct:identifier "animations_bistrots_de_pays" ;
    dct:language <http://id.loc.gov/vocabulary/iso639-1/fr> ;
    dct:publisher [ a foaf:Agent ;
            rdfs:label "Example datasets" ] ;
    dct:title "example datasets" ;
    dcat:distribution <https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-csv>,
        <https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-geojson>,
        <https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-json>,
        <https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-shp> .

<https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-csv> a dcat:Distribution ;
    dct:description "csv export of https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays" ;
    dct:format "csv" ;
    dct:license "http://opendatacommons.org/licenses/odbl/1.0/" ;
    dcat:accessURL <https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays/exports/csv> ;
    dcat:mediaType "text/csv" .

<https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-geojson> a dcat:Distribution ;
    dct:description "geojson export of https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays" ;
    dct:format "geojson" ;
    dct:license "http://opendatacommons.org/licenses/odbl/1.0/" ;
    dcat:accessURL <https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays/exports/geojson> ;
    dcat:mediaType "application/json" .

<https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-json> a dcat:Distribution ;
    dct:description "json export of https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays" ;
    dct:format "json" ;
    dct:license "http://opendatacommons.org/licenses/odbl/1.0/" ;
    dcat:accessURL <https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays/exports/json> ;
    dcat:mediaType "application/json" .

<https://example.com/api/v2/catalog/datasets/<theRandomCode>/animations_bistrots_de_pays-shp> a dcat:Distribution ;
    dct:description "shp export of https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays" ;
    dct:format "shp" ;
    dct:license "http://opendatacommons.org/licenses/odbl/1.0/" ;
    dcat:accessURL <https://example.com/api/v2/catalog/datasets/animations_bistrots_de_pays/exports/shp> ;
    dcat:mediaType "application/zip" ."""

ac = ""
num = 27050
for i in range(1,num+1):
	print i
	ran = str(random.getrandbits(30))
	ac = ac + placeHolder.replace("<theRandomCode>",ran)
	if (i % 50 == 0):
		final = top + ac
		f = open("datasets/"+str(i),"w")
		f.write(top+ac)
		f.close()
