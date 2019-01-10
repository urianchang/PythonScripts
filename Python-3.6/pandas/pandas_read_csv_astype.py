# Python 3.6
import io
import pandas as pd

INPUT_DATA = """\
timestamp,counter,accession number,completion,genus,species
2018-09-13 12:01:00,1,12345,88,Anopheles,gambiae
2018-09-13 12:11:00,2,23456,75,Stegosaurus,stenops
2018-09-13 12:21:00,3,34567,68,Ankylosaurus,magniventris
2018-09-13 12:31:00,4,45678,90,Raphus,cucullatus
2018-09-13 12:41:00,5,56789,100,Deinonychus,antirrhopus
2018-09-13 12:51:00,6,67890,99,Achillobator,giganticus
2018-09-13 13:01:00,7,98778,76,Brontosaurus,excelsus
2018-09-13 13:11:00,8,12346,84,Aedes,aegypti
2018-09-13 13:21:00,9,88888,89,Tyrannosaurus,rex
"""

df = pd.read_csv(io.StringIO(INPUT_DATA), header=0, index_col=None)
df["locus_name"] = df["accession number"].astype(str) \
                   + df["genus"].astype(str).str[0].str.upper() \
                   + df["species"].astype(str).str[0].str.upper()

print(df)
