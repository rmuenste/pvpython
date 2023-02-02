import sys
import os
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName1", help="Input file name 1")
    parser.add_argument("resultName", help="Name of result file")
    parser.add_argument("steps", help="Number of steps", type=int)
    args = parser.parse_args()

    print(args)
    steps = args.steps
    u1 = np.loadtxt(args.fileName1)
    u = (u1) / steps
    np.savetxt(args.resultName, u)

if __name__ == "__main__":
    main()
