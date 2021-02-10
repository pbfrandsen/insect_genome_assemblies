import sys
import csv

filename = sys.argv[1]
taxon_name = filename.split(".")[0]
outfilename = sys.argv[2]
accession_filename = sys.argv[3]

revised_accessions = set()
accessions = set()
genome_number = 0
chrom_genome_number = 0
contig_n50_greater = 0

with open(accession_filename) as access_file:
    for line in access_file:
        revised_accessions.add(line.strip())

with open(filename) as infile:
    with open(outfilename, "a") as outfile:
        csvfile = csv.reader(infile)
        for count,line in enumerate(csvfile):
            if count > 0:
                accession = line[2]
                # print("This is the accession: " + accession + "\n")
                assembly_level = line[4]
                # print("This is the assembly level: " + assembly_level + "\n")
                contig_n50 = line[6]
                # print("This is the contig N50: " + contig_n50 + "\n")
                display_name = line[7]
                extra_stuff = line[9].split(",")
                length = line[10]
                date = line[-1].strip()
                for item in extra_stuff:
                    if "sci_name" in item:
                        species_name = item.split(": ")[1]
                if accession in revised_accessions:
                    accessions.add(accession)
                    genome_number += 1
                    if assembly_level == "Chromosome":
                        chrom_genome_number += 1
                    if int(contig_n50) > 999999:
                        contig_n50_greater += 1
                    outfile.write(taxon_name + "," + str(species_name) + "," + 
                        str(display_name) + "," + str(accession) + "," + 
                        str(contig_n50) + "," + str(assembly_level) + "," +
                        str(length) + "," + str(date) + "\n")


    

