"""
This script appends a data array from a file to a set of .vtu files

Example launch command from a bash console
#//========================================
#for((i=2;i<=27;i++)); do name=$(printf "res_node_%03d.00000.vtu" $i); name2=$(printf "u_avg_%03d_part_0-10000.txt" $i); ~/anaconda3/python.exe append_array_vtk.py $name $name2; done
"""
import os
import re
import sys
import glob
import copy
import argparse
import numpy as np
import xml.etree.ElementTree as ET

def parseVtu(fileName, arrayName, outDir):
    tree = ET.parse(fileName)
    root = tree.getroot()

    uavg = np.loadtxt(arrayName)
    my_string = np.array2string(uavg[0])
    print(f"My string converted from array: {my_string}")

    values = ""
    for i in uavg:
        i = i 
        values = values + f"{i[0]} {i[1]} {i[2]}\n"

    elems = [elem.tag for elem in root.iter()]
    #print(elems) res_node_001.00000.vtu u_avg_001_part_0-10000.txt

    pressV = ""
    vel = "" 

    for bla in root.iter():
        if bla.tag =="DataArray":
            if bla.attrib['Name'] == 'Velocity':
                vel = copy.deepcopy(bla) 
                vel.attrib['Name'] = 'U_bar'
                vel.text = values 

    for bla in root.iter():
        if bla.tag =="PointData":
            bla.append(vel)
            #nodeList = vel.text.splitlines()
            #nodeList = list(filter(lambda x: (len(x.strip()) > 0), nodeList))
            #print(nodeList)
            #vel.text = "\n".join(nodeList)
        
    tree.write("%s/%s" %(outDir, fileName))

def writeParsed(vel, press, fileName):
    with open(fileName, "w") as f:
        for idx, item in enumerate(press):
            f.write("%s %s %s %s\n" %(press[idx], vel[idx][0], vel[idx][1], vel[idx][2]))

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", help="Name of the target .vtu file")
    parser.add_argument("arrayName", help="Name of the file that contains the data set to be appended")
    parser.add_argument("-d", "--outdir", help="Name of the output directory", nargs='?', const=1, type=str, default="sampleDir")
    args = parser.parse_args()

    print(args)
    parseVtu(args.fileName, args.arrayName, args.outdir)

if __name__ == "__main__":
    main()
