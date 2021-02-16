# Insect genome assembly stats
scripts used to download and analyze insect assemblies from GenBank
These scripts were used to download and organize insect genome assembly metadata from NCBI.

`download_insect_data.sh` is a simple shell scrip that uses the [ncbi datasets](https://www.ncbi.nlm.nih.gov/datasets/) (v. 10.9.0) command line tool to download individual `json` files for each insect order.

`convert2csv.py` uses pandas to convert the `json` file to a `csv`.

`extract_genome_stats.py` extracts some relevant statistics from the csv files and organizes them into a new output file.

`scrape_assembly_info.py` is a webscraping script that uses [beautiful soup](https://pypi.org/project/beautifulsoup4/) to find metadata that isn't included in the datasets tool (sequencing coverage, sequencing technology, assembler used).

You can run `scrape_assembly_info.py` over a list of accession numbers in a text file with, e.g. ```for i in `cat accessions.txt`; do python scrape_assembly_info.py $i; done``` The resulting data will be written to a file called `assembly_type.csv`.

#### Figure 2 a,b scripts
**Fig2a_data.txt**

A modified of the big data frame I used for the plot in Fig. 2a. This file is read by the `Fig_2a_b_plotter.R` script.

**Fig2b_parse.py**

A python script that parses the above file and ouputs a subset of the data formatted for plotting the BUSCO plot in 2b.

**Fig2b_data.txt**

The file produced by running the above python script. This file is read by the `Fig_2a_b_plotter.R` script to produce plot 2b (BUSCOs).

**Fig_2a_b_plotter.R**

The R script that plots 2a using `Fig2a_data.txt` as input, and 2b using `Fig2b_data.txt` as input.