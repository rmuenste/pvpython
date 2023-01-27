import os
import re
import sys
import glob
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
def parseVtu(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    elems = [elem.tag for elem in root.iter()]
    #print(elems)

    pressV = ""
    vel = "" 
    for bla in root.iter():
        if bla.tag =="DataArray":
            if bla.attrib['Name'] == 'Velocity':
                vel = bla.text.split()
                vel = list(zip(vel[::3], vel[1::3], vel[2::3]))
                #del vel[::5]
                #vel = vel[::5]
    for i in range(len(vel)):
        vel[i] = [float(x) for x in vel[i]]
        
    v = np.array(vel)
    return v

def writeParsed(vel, press, fileName):
    with open(fileName, "w") as f:
        for idx, item in enumerate(press):
            f.write("%s %s %s %s\n" %(press[idx], vel[idx][0], vel[idx][1], vel[idx][2]))

def processFiles(res, steps, procs):

    for j in range(1, 2):
        inputName = res[0]
        file, ext = os.path.splitext(inputName)
        id = file[17:]
        name = "res_node_%03d.%s.vtu" %(j,id)
        print(name)
        u_avg = parseVtu(name)
        for i in range(1,len(res)):
            inputName = res[i] 
            file, ext = os.path.splitext(inputName)
            id = file[17:]
            name = "res_node_%03d.%s.vtu" %(j,id)
            print(name)
            v = parseVtu(name)
            u_avg = u_avg + v
#            print(len(v), v.shape)

        np.savetxt("u_avg_%03d.txt" %(j), u_avg)

def processFileList(fileName, off, steps, procs):

    res = []
    with open(fileName, 'r') as f:
        res = f.readlines()

    print(res)
    for j in range(1, procs+1):
        inputName = res[off].strip()
        name = "res_node_%03d.%s.vtu" %(j,inputName)
        print(name)
        u_avg = parseVtu(name)
        for i in range(off+1, off + steps):
            inputName = res[i].strip() 
            name = "res_node_%03d.%s.vtu" %(j,inputName)
            print(name)
            v = parseVtu(name)
            u_avg = u_avg + v
#            print(len(v), v.shape)

        partId = "%d-%d" %(off,off+steps-1)
        np.savetxt("u_avg_%03d_part_%s.txt" %(j, partId), u_avg)

def main():
    # args: offset step 
    if len(sys.argv) <= 1:
        print(sys.argv)
        files = r'd:\work\avg\main.*.pvtu'
        res = glob.glob(files)
        steps = len(res)
        processFiles(res, steps, 2)
    else:
        print("here")
        processFileList(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

#    print(res[0])
#    for j in range(1, 2):
#        inputName = res[0]
#        file, ext = os.path.splitext(inputName)
#        id = file[17:]
#        name = "res_node_%03d.%s.vtu" %(j,id)
#        print(name)
#        u_avg = parseVtu(name)
#        for i in range(1,len(res)):
#            inputName = res[i] 
#            file, ext = os.path.splitext(inputName)
#            id = file[17:]
#            name = "res_node_%03d.%s.vtu" %(j,id)
#            print(name)
#            v = parseVtu(name)
#            u_avg = u_avg + v
##            print(len(v), v.shape)
#
#        np.savetxt("u_avg_%03d.txt" %(j), u_avg)

#    inputName = sys.argv[1]
#    file, ext = os.path.splitext(inputName)
#    outputName = "./sampleData/piece_%s.dat" %(file[13:])
#    print(inputName)
#    print(outputName)
#    (v, p) = parseVtu(inputName)
#    writeParsed(v, p, outputName)
#    print(len(p))
#    print(len(v))

if __name__ == "__main__":
    main()
