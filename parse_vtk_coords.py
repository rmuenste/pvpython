'''
This script parses a .vtu file and extracts the velocity and pressure and then writes these
to a "piece" file in the format
0 velocity_x velocity_y velocity_z pressure
1 velocity_x velocity_y velocity_z pressure
2 velocity_x velocity_y velocity_z pressure
3 velocity_x velocity_y velocity_z pressure

Example launch command from a bash console
#//========================================
#for i in vtk2/main.00000.pvtu; do b=${i:10:5}; for((j=1;j<=27;j++)); do name=$(printf "res_node_%03d.%s.vtu" $j $b); python3 ./parse_vtk2.py "vtk2/$name"; done; done

...
'''
import os
import re
import sys
import argparse
import xml.etree.ElementTree as ET

def parseVtu(fileName):
    """
    Parse the vtu file into an etree structure
    """
    tree = ET.parse(fileName)
    root = tree.getroot()

    elems = [elem.tag for elem in root.iter()]
    #print(elems)

    coords = ""
    for bla in root.iter():
        if bla.tag =="DataArray":
#            print(bla.attrib['Name'])
            if bla.attrib['Name'] == 'Points':
                coords = bla.text.split()
                coords = list(zip(coords[::3], coords[1::3], coords[2::3]))
                #del vel[::5]
                coords = coords[::5]

    return coords

def writeParsed(coords, fileName):
    """
    Writes the coordinates array into a file
    """
    with open(fileName, "w") as f:
        for idx, item in enumerate(coords):
            f.write("%s %s %s\n" %(coords[idx][0], coords[idx][1], coords[idx][2]))

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("inputName", help="Path to the input .vtu file")
    parser.add_argument("outputDir", help="Path to the output directory where the resulting .dat files are stored")
    args = parser.parse_args()

    inputName = args.inputName 
    file, ext = os.path.splitext(inputName)
    fileBase = os.path.basename(file)
    outDir = args.outputDir 
    outputName = "%s/c_piece_%s.dat" %(outDir, fileBase[9:])

    print("Processing: %s" %(os.path.basename(outputName)))
#    print("sys argv: ",inputName)
#    print("out name: ",outputName)

    coords = parseVtu(inputName)
    writeParsed(coords, outputName)

if __name__ == "__main__":
    main()

