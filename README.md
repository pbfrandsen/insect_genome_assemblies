# insect_genome_assemblies
scripts used to download and analyze insect assemblies from GenBank
These scripts were used to download and organize insect genome assembly metadata from NCBI.

`download_insect_data.sh` is a simple shell scrip that uses the [ncbi datasets](https://www.ncbi.nlm.nih.gov/datasets/) (v. 10.9.0) command line tool to download individual `json` files for each insect order.

`convert2csv.py` uses pandas to convert the `json` file to a `csv`.

`extract_genome_stats.py` extracts some relevant statistics from the csv files and organizes them into a new output file.

`scrape_assembly_info.py` is a webscraping script that uses [beautiful soup](https://pypi.org/project/beautifulsoup4/) to find metadata that isn't included in the datasets tool (sequencing coverage, sequencing technology, assembler used).

