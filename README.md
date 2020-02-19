# search_pubmed_entrez
Searches for articles in PubMed using an user input (allows field tags). And outputs an Excel table with the results.
This scripts uses BioPython and Entrez.


### AUTHOR AND CONTACT
Script made by David Requena [02/19/2020]

The Rockefeller University. New York, USA.

Contact: drequena@rockefeller.edu / d.requena.a@gmail.com


### DESCRIPTION
This code asks the user for a query to be searched in PubMed. This can include Field Tags:
https://www.ncbi.nlm.nih.gov/books/NBK3827/#pubmedhelp.Search_Field_Descriptions_and

Then, it retrieves the PubMed ID (PMID), e-publication date, the title, journal
list of authors (separated by semicolon), DOI and language.
And finally saves the info in a table (in MS Excel .xlsx format) in the current directory.


### REQUISITES
You need to have installed Python 3 (https://www.python.org/downloads/) and the following modules:

1. pandas -> can be installed by writting in the Terminal: pip install pandas
2. biopython -> can be installed by writting in the Terminal: pip install biopython
3. openpyxl -> can be installed by writting in the Terminal: pip install openpyxl


### USAGE
Just doble-click on the script to execute it. This can also be called from the Terminal.
Then, the program will ask you to:

First, provide a query. Here you have two equivalent examples:

    Example 1: (Fowlpox OR FPV) AND (Reticuloendotheliosis OR REV)
    Example 2: (Fowlpox[All Fields] OR FPV[All Fields]) AND (Reticuloendotheliosis[All Fields] OR REV[All Fields])

Second, provide an e-mail address (optional). You can just say no.

Third, the maximum number of results desired.

I'm including an example of the output table.


### REFEFENCE:
Description of the Entrez package:
1. https://biopython.org/DIST/docs/api/Bio.Entrez-module.html?fbclid=IwAR1SU1aXV64JJKpFwjy4Dqbf0hGdguOAubGLPVHes8U_wrKMnQE-GuIdPwo
