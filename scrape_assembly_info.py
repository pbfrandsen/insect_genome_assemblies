# The variables that we want to parse are:
# Assembly method, Genome coverage, and Sequencing technology
# Written by Ashlyn Powell and Paul Frandsen
import sys
import csv
import requests
from bs4 import BeautifulSoup

# accession number fed as the first argument
accession = sys.argv[1]

# URL, the unique thing among genomes is the GCA_*** part
URL = 'https://www.ncbi.nlm.nih.gov/assembly/' + accession
page = requests.get(URL)

# Parse the contents of the URL with Beautiful Soup
soup = BeautifulSoup(page.content, 'html.parser')

# Assign the "summary_cont" div to summary_continued variable
summary_continued = soup.find(id="summary_cont")

# Make the summary easier to read
pretty_summary = summary_continued.prettify()

# Pretty_summary is a string, use split to parse into list
bits = pretty_summary.strip().split("  ")


assembly_index = False
genome_index = False
sequencing_index = False

# loop through list, get index of desired info
for i, item in enumerate(bits):
    if "Assembly method:" in item:
        assembly_index = i + 6 #6 is the magic number to add for this URL, hopefully it's the same for the rest
    elif "Genome coverage" in item:
        genome_index = i + 6
    elif "Sequencing technology" in item:
        sequencing_index = i + 6

# for num in range(20):
    #print(bits[genome_index + num])

# get info using index, print to verify, store in dictionary
if assembly_index != False:
    assembly_info = bits[assembly_index].strip()
else:
    assembly_info = "N/A"

if genome_index != False:
    genome_info = bits[genome_index].strip()
else:
    genome_info = "N/A"

if sequencing_index != False:
    sequencing_info =  bits[sequencing_index].strip()
else:
    sequencing_info = "N/A"

print("Accession: " + accession)
print("Assembler: " + assembly_info)
print("Genome coverage: " + genome_info)
print("Sequencing technology: " + sequencing_info)

fields = ['Accession', 'Assembler', 'Genome coverage', 'Sequencing technology']
rows = [accession, assembly_info, genome_info, sequencing_info]
mydict =[{'Accession': accession, 'Assembler': assembly_info, 'Genome coverage': genome_info, 'Sequencing technology': sequencing_info}]
filename = "assembly_type.csv"

# writing to csv file  
with open(filename, 'a') as csvfile:  
    # creating a csv dict writer object  
    writer = csv.DictWriter(csvfile, fieldnames = fields)  
        
    # writing headers (field names)  
    # writer.writeheader()  
        
    # writing data rows  
    writer.writerows(mydict)