import os
import re
import sys
import xml.etree.ElementTree as ET
#for i in piece_???.00000.dat; do cat $i >> all_00000.data; done
#for((i=0;i<=10000;i=i+50)); do for((j=1;j<=48;j++)); do name=$(printf "res_node_%03d.%05d.vtu" $j $i); echo $name; done; done
#for((i=0;i<=1000;i=i+50)); do for((j=1;j<=48;j++)); do name=$(printf "res_node_%03d.%05d.vtu" $j $i); python3 ./parse_vtk.py "_vtk/$name"; done; done
#1000
#for((i=0;i<=1000;i=i+50)); do for((j=1;j<=48;j++)); do name1=$(printf "piece_%03d.%05d.dat" $j $i); name2=$(printf "step_%05d.res" $i); echo $name1; cat $name1 >> $name2; done; done
#_vtk/res_node_000.
def parseVtu(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    elems = [elem.tag for elem in root.iter()]
    #print(elems)

    pressV = ""
    vel = ""
    for bla in root.iter():
        if bla.tag =="DataArray":
#            print(bla.attrib['Name'])
            if bla.attrib['Name'] == 'Pressure_V':
                pressV = bla.text.split()
                print(len(pressV))
                #del pressV[::5]
                pressV = pressV[::5]
            if bla.attrib['Name'] == 'Velocity':
                vel = bla.text.split()
                vel = list(zip(vel[::3], vel[1::3], vel[2::3]))
                #del vel[::5]
                vel = vel[::5]

    return vel, pressV

def writeParsed(vel, press, fileName):
    with open(fileName, "w") as f:
        for idx, item in enumerate(press):
            f.write("%s %s %s %s\n" %(press[idx], vel[idx][0], vel[idx][1], vel[idx][2]))

def main():
    inputName = sys.argv[1]
    file, ext = os.path.splitext(inputName)
    outputName = "./sampleData2/piece_%s.dat" %(file[14:])
    print(inputName)
    print(outputName)
    (v, p) = parseVtu(inputName)
    writeParsed(v, p, outputName)
    print(type(p))
    print(len(p))
    print(len(v))

if __name__ == "__main__":
    main()
