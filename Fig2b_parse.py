#! /usr/local/bin/python3

##this script was used to parse the data table "Fig2a_data.txt" and output relevant
##data in the correct format to produce the plot in Fig. 2B. Written by John Sproul
import sys

data_filename = sys.argv[1]
outfilename = sys.argv[2]

cat_s = "dS"
cat_d = "cD"
cat_f = "bF"
cat_m = "aM"
with open(outfilename, "a") as outfile:
	outstring1 = '{}\t{}\t{}\n'.format("name", "value","category")
	outfile.write(outstring1)
	N=0
	with open (data_filename, 'r') as name_data:

		for Line in name_data:
			elif N>=0:
				#file_name = Line
				#print (file_name)
				stripped = Line.strip ('\n') #strips out new line characters
				#print(stripped)
				parsed = stripped.split ('\t')
				species_name = parsed[5]
				single_val = parsed[9]
				dup_val = parsed[10]
				frag_val = parsed[11]
				missing_val = parsed[12]
			
				outstring2 = '{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}\n'.format(species_name, single_val, cat_s, species_name, dup_val, cat_d, species_name, frag_val, cat_f, species_name, missing_val, cat_m)
				#print (Outstring)
				outfile.write(outstring2)
				N += 1
			
			
print ("done")
		