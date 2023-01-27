import os
import re
import sys
import glob
import numpy as np
import xml.etree.ElementTree as ET

def main():

    print(sys.argv)
    if len(sys.argv) < 3:
        sys.exit("Needs at least 2 arguments: partial_sums.py 1 3")

    part = int(sys.argv[1])
    timeSteps = int(sys.argv[2])

    first = 'u_avg_%03d_part_' %part
    files =  first + '*.txt'
    res = glob.glob(files)
    steps = len(res)
    print(res)
    if steps == 0:
        sys.exit("no file match") 

    u_avg = np.loadtxt(res[0])
    for i in range(1, len(res)):
        u = np.loadtxt(res[i])
        u_avg = u_avg + u

    u_avg = u_avg / timeSteps
    name = 'u_avg_%03d_total.dat' %part
    np.savetxt(name, u_avg)




if __name__ == "__main__":
    main()
