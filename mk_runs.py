#! /usr/bin/env python
#
#   script generator 


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-MX-40"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["HATLAS-L9"] = [ 106745, 106746, 106747, 106749, 106750, 106751, 106753,
                    106754, 106755, 106758, 106759, 106760, 106864, 106865,
                    106866, 106868, 106869, 106870, 106872, 106873, 106874,
                    106877, -106878, 106879,]

pars1 = {}
pars1["HATLAS-L9"] = "speczoom=91,3 badcb=3/3,3/4" 

pars2 = {}
pars2["HATLAS-L9"] = "srdp=1 admit=0"


if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, sys.argv)

