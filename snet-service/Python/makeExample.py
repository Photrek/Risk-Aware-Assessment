import numpy as np

filename = "data.csv"
NR = 1000
NC = 4   # number of columns (NOT including class), so effectively #classes

# CONVENTION: no header
with open("data.csv","wt") as f:
    for iR in range(NR):
        for iC in range(NC):
            f.write(f"{np.random.rand()},")
        f.write(f"{np.random.randint(NC)+1}\n")  # CONVENTION: category is 1-indexed (values [1,NC])