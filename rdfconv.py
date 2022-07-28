import os
import sys

from rdflib import Graph
from tabulate import tabulate

formats = {
    ".jsonld": "json-ld",
    ".n3": "n3",
    ".nt": "nt",
    ".rdf": "xml",
    ".owl": "xml",
    ".xml": "xml",
    ".trig": "trig",
    ".ttl": "turtle"
}

########################################################################
# ERROR MESSAGES
########################################################################

n = len(sys.argv)

if n < 3:
    print("\nUsage: rdfconv <input file or URL> <output file>. The allowed input and output file formats are: \n")
    print(tabulate(
        [['JSON-LD', '.jsonld'], ['N3', '.n3'], ['N-Triples', '.nt'], ['RDF/XML', '.rdf'],
         ['RDF/XML', '.owl'], ['RDF/XML', '.xml'], ['TriG', '.trig'], ['Turtle', '.ttl']],
        headers=['Syntax', 'File Extension']))
    print("")
    exit(1)

########################################################################
# EXECUTION
########################################################################

g = Graph()

try:
    g.parse(sys.argv[1])
except OSError:
    print(f"\nCould not READ file {sys.argv[1]}. Please provide a valid input file. Exiting program.\n")
    exit(1)

target_extension = os.path.splitext(sys.argv[2])[1]

if target_extension in formats:
    try:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(g.serialize(format=formats[target_extension]))
    except OSError:
        print(f"\nCould not WRITE file {sys.argv[2]}. Exiting program.\n")
        exit(1)
else:
    print("\nPlease provide a valid output file name. The allowed input and output file formats are: \n")
    print(tabulate(
        [['JSON-LD', '.jsonld'], ['N3', '.n3'], ['N-Triples', '.nt'], ['RDF/XML', '.rdf'],
         ['RDF/XML', '.owl'], ['RDF/XML', '.xml'], ['TriG', '.trig'], ['Turtle', '.ttl']],
        headers=['Syntax', 'File Extension']))
    print("\nExiting program.\n")
    exit(1)
