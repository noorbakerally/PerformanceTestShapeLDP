import sys
filename = sys.argv[1]

from rdflib import Graph
g = Graph()
g.parse(filename,format="turtle")
print len(g)

