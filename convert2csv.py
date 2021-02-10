import sys
import pandas as pd

filename = sys.argv[1]
outfilename = filename.split(".")[0] + ".csv"

df = pd.read_json(filename)
df.to_csv(outfilename)
