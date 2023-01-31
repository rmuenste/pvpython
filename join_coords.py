'''
This script appends the lines of one file to a second file

Example launch command from a bash console
#//========================================
#for i in vtk2/main.00000.pvtu; do b=${i:10:5}; for((j=1;j<=27;j++)); do name=$(printf "res_node_%03d.%s.vtu" $j $b); python3 ./parse_vtk2.py "vtk2/$name"; done; done

...
'''
import os
import re
import sys
import argparse

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="The source file that should be pasted in to the destination file")
    parser.add_argument("destination", help="The destination file that should be pasted in to the source file")
    args = parser.parse_args()

    with open(args.source, "r") as source:
        lines = source.readlines()

    with open(args.destination, "a") as dest:
        for line in lines:
            dest.write(line + "\n")

if __name__ =="__main__":
    main()