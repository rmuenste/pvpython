import os
import re
import sys
import glob
import copy
import numpy as np
import xml.etree.ElementTree as ET
#for i in piece_???.00000.dat; do cat $i >> all_00000.data; done
#for((i=0;i<=10000;i=i+50)); do for((j=1;j<=48;j++)); do name=$(printf "res_node_%03d.%05d.vtu" $j $i); echo $name; done; done
#for((i=0;i<=1000;i=i+50)); do for((j=1;j<=48;j++)); do name=$(printf "res_node_%03d.%05d.vtu" $j $i); python3 ./parse_vtk.py "_vtk/$name"; done; done
#1000
#for((i=0;i<=1000;i=i+50)); do for((j=1;j<=48;j++)); do name1=$(printf "piece_%03d.%05d.dat" $j $i); name2=$(printf "step_%05d.res" $i); echo $name1; cat $name1 >> $name2; done; done
#_vtk/res_node_000.
#~/anaconda3/python.exe u_avg_vtk.py files.dat 2 1 27
#for i in {1..27}; do ~/anaconda3/python.exe partial_sums.py $i 3; done
#for((i=2;i<=27;i++)); do name=$(printf "res_node_%03d.00000.vtu" $i); name2=$(printf "u_avg_%03d_part_0-10000.txt" $i); ~/anaconda3/python.exe append_array_vtk.py $name $name2; done
def parseVtu(fileName, arrayName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    uavg = np.loadtxt(arrayName)
    my_string = np.array2string(uavg[0])
    print(f"My string converted from array: {my_string}")

    values = ""
    for i in uavg:
        i = i / 10001
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
        
    tree.write("sampleDir/%s" %fileName)

def writeParsed(vel, press, fileName):
    with open(fileName, "w") as f:
        for idx, item in enumerate(press):
            f.write("%s %s %s %s\n" %(press[idx], vel[idx][0], vel[idx][1], vel[idx][2]))

def main():
    # args: offset step 
    if len(sys.argv) > 1:
        print(sys.argv)
        fileName = sys.argv[1]
        arrayName = sys.argv[2]
        parseVtu(fileName, arrayName)

if __name__ == "__main__":
    main()
