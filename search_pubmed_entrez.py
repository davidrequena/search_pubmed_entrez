#--------------------#
# AUTHOR AND CONTACT #
#--------------------#
# Script made by David Requena [02/19/2020]
# The Rockefeller University. New York, USA.
# Contact: drequena@rockefeller.edu / d.requena.a@gmail.com

#-------------#
# DESCRIPTION #
#-------------#
# This code asks the user for a query to be searched in PubMed. This can include Field Tags:
# https://www.ncbi.nlm.nih.gov/books/NBK3827/#pubmedhelp.Search_Field_Descriptions_and
# Then, it retrieves the PubMed ID (PMID), e-publication date, the title, journal
# list of authors (separated by semicolon), DOI and language.
# And finally saves the info in a table (in MS Excel .xlsx format) in the current directory.

#------------#
# REQUISITES #
#------------#
# You need to have installed Python 3: https://www.python.org/downloads/
# And the following modules:
# 1. pandas -> can be installed by writting in the Terminal: pip install pandas
# 2. biopython -> can be installed by writting in the Terminal: pip install biopython
# 3. openpyxl -> can be installed by writting in the Terminal: pip install openpyxl

#-------#
# USAGE #
#-------#
# Just doble-click on the script to execute it. This can also be called from the Terminal.
# Then, the program will ask you to:
#
# First, provide a query. Here you have two equivalent examples:
#
#     Example 1: (Fowlpox OR FPV) AND (Reticuloendotheliosis OR REV)
#     Example 2: (Fowlpox[All Fields] OR FPV[All Fields]) AND (Reticuloendotheliosis[All Fields] OR REV[All Fields])
#
# Second, provide an e-mail address (optional). You can just say no.
# Third, the maximum number of results desired.
#
# I'm including an example of the output table.

#-----------#
# REFEFENCE #
#-----------#
# Description of the Entrez package:
# https://biopython.org/DIST/docs/api/Bio.Entrez-module.html?fbclid=IwAR1SU1aXV64JJKpFwjy4Dqbf0hGdguOAubGLPVHes8U_wrKMnQE-GuIdPwo


import pandas as pd
from Bio import Entrez
import time

# User inputs:
query = input("Provide a query for PubMed (can include field tags): ")
my_email = input("Provide your e-mail address: ")
max_results = input("Maximum number of results: ")

# Consult PubMed:
Entrez.email = my_email
handle_search = Entrez.esearch('pubmed', term = query, retmax = max_results)
results = Entrez.read(handle_search)
handle_search.close()

# Create an empty Dataframe with just the column names:
articles_df = pd.DataFrame(columns = ['PMID',
                                      'ePublication_date',
                                      'Title',
                                      'Journal_Abbrev',
                                      'Authors',
                                      'Journal',
                                      'DOI',
                                      'Language'])

for article_id in results['IdList']:
    handle_retrieve = Entrez.esummary(db = 'pubmed', id = article_id, retmode = 'xml')
    article = Entrez.read(handle_retrieve)
    handle_retrieve.close()

    # Collect the article info
    articles_df = articles_df.append({u'PMID': article[0]['Id'],
                                      u'ePublication_date': article[0]['EPubDate'],
                                      u'Title': article[0]['Title'],
                                      u'Journal_Abbrev': article[0]['Source'],
                                      u'Authors': '; '.join(article[0]['AuthorList']),
                                      u'Journal': article[0]['FullJournalName'],
                                      u'DOI': article[0]['DOI'],
                                      u'Language': article[0]['LangList']}, ignore_index=True)

# Print the top 5 rows of the dataframe:
print("First 5 results:")
print(articles_df.head(5))

# Export the list of articles as an Excel file with a timestamp
output_file = 'table_of_articles_' + time.strftime("%m%d%Y-%H%M%S") + '.xlsx'
print("A table named " + output_file + " with the search results has been saved in the current directory.")
articles_df.to_excel(output_file)

# In Mac OS X, if the following error happens:
# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]
# certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)>
# Try this: https://stackoverflow.com/questions/50236117/
