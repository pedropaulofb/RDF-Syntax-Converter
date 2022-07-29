# RDF Syntax Converter <!-- omit in toc -->

A small and simple RDF syntax converter built in Python using the RDFLib.

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Limitations](#limitations)
- [Software requirements](#software-requirements)
- [Code execution](#code-execution)
- [Usage examples](#usage-examples)
- [Contributions](#contributions)

## Overview

[RDF](https://www.w3.org/RDF/) is a standard model for data interchange on the Web, standardized by the [World Wide Web Consortium (W3C)](https://www.w3.org/).

The following table presents the allowed input and output RDF syntaxes. I.e., the **RDF Syntax Converter** can convert from and to the following syntaxes:

| **Allowed Syntax** 	| **File Extension** 	|
|--------------------	|--------------------	|
| JSON-LD            	| .jsonld            	|
| N3                 	| .n3                	|
| N-Triples          	| .nt                	|
| RDF/XML            	| .rdf, .owl, .xml     	|
| TriG               	| .trig              	|
| Turtle             	| .ttl               	|


The software accepts as input any URL or file formatted in one of the mentioned syntaxes and generates a file with the desired target syntax as output.

## Limitations

This software is a simple implementation of an RDF syntax converter that relies on the [RDFLib](https://pypi.org/project/rdflib/) v6.2.0 capabilities. It was created for training purposes and, hence, no refinements were performed.

The software was not extensively tested and does not count with advanced errors and exceptions handlings or even non-standard use verifications. The software was developed in a Windows environment and was not tested in Linux or Mac.

## Software requirements

You need to [download and install Python](https://www.python.org/downloads/) for executing the **RDF Syntax Converter**. The code was developed and tested using [Python](https://www.python.org/) v3.10.5.

Only two external libraries are necessary: [RDFLib](https://pypi.org/project/rdflib/) (v6.2.0) and [Tabulate](https://pypi.org/project/tabulate/) (v0.8.10). For installing these libraries, run the following command on the terminal:

```shell
pip install -r requirements.txt
```

## Code execution

After the external libraries are installed, run the following command on the terminal for executing the **RDF Syntax Converter**:

```shell
python rdfconv.py <input file OR URL> <output file>
```

While the input syntax is automatically detected by the **RDF Syntax Converter**, the target syntax is chosen via the output filetype (file extension) informed by the user as the software argument.

## Usage examples

Converting a web RDF-based file to a JSON-LD file (saved in the same directory of the rdfconv.py file):

```shell
python rdfconv.py http://purl.org/nemo/gufo gufo.jsonld
```

Converting an OWL file formatted in XML/RDF to a Turtle (TTL) file (both input and output files are saved in the same directory of the rdfconv.py file):

```shell
python rdfconv.py ontology.rdf ontology.ttl
```

## Contributions
Every contribution is very welcomed!

Problem reporting, new feature requests, questions, or ideas can be sent through this repository’s [issues section](https://github.com/pedropaulofb/RDF-Syntax-Converter/issues). Coding contributions are also accepted and can be done via the repository’s [PR section](https://github.com/pedropaulofb/RDF-Syntax-Converter/pulls).

This is a free open-source project. If you use it and like it, you can buy me a coffee =)

<a href="https://www.buymeacoffee.com/pedropaulofb"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=pedropaulofb&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>