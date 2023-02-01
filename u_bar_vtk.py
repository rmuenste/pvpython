"""
This script computes the average velocity of a given .vtu file series
"""
import os
import re
import sys
import glob
import argparse
import numpy as np
import xml.etree.ElementTree as ET

#~/anaconda3/python.exe u_avg_vtk.py files.dat 2 1 27
#for i in {1..27}; do ~/anaconda3/python.exe partial_sums.py $i 3; done
#python pvpython/u_bar_vtk.py -f "D:\\work\\avg\\sampleVtk\\main.*.pvtu" -p 1-27

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

def extractFileNumber(files):
    fileList = []
    for file in files:
        fileBase = os.path.basename(file)
        fileName, ext = os.path.splitext(fileBase)
        dirName = os.path.dirname(file)
        idx = fileName.split('.')[1]
        fileList.append(idx)
    return fileList

def calcSize(files, idx):
    pidx = idx
    if len(files) >= 1:
        file = files[0]
        fileBase = os.path.basename(file)
        fileName, ext = os.path.splitext(fileBase)
        dirName = os.path.dirname(file)
        fidx = fileName.split('.')[1]

        name1 = "res_node_%03d.%s.vtu" %(pidx, fidx)
        name = os.path.join(dirName, name1)
        u_bar = parseVtu(name)
        return u_bar.shape

def processListProcs(files, idxStart, idxEnd):

    fileNumbers = extractFileNumber(files)
    partId = "%s-%s" %(fileNumbers[0],fileNumbers[len(files)-1])
    for pidx in range(idxStart, idxEnd+1):
        size = calcSize(files, pidx)
        u_bar = np.zeros(size)
        for file in files:
            fileBase = os.path.basename(file)
            fileName, ext = os.path.splitext(fileBase)
            dirName = os.path.dirname(file)
            fidx = fileName.split('.')[1]

            name1 = "res_node_%03d.%s.vtu" %(pidx, fidx)
            name = os.path.join(dirName, name1)
            print(name)
            u = parseVtu(name)
            u_bar = u_bar + u

        np.savetxt("u_avg_%03d_part_%s.txt" %(pidx, partId), u_bar)

#            fileBase = os.path.basename(file)
#            outDir = args.outputDir 
#            outputName = "%s/c_piece_%s.dat" %(outDir, fileBase[9:])

#        inputName = res[off].strip()
#        name = "res_node_%03d.%s.vtu" %(j,inputName)
#        print(name)
#        u_avg = parseVtu(name)
#        for i in range(off+1, off + steps):
#            inputName = res[i].strip() 
#            name = "res_node_%03d.%s.vtu" %(j,inputName)
#            print(name)
#            v = parseVtu(name)
#            u_avg = u_avg + v
##            print(len(v), v.shape)
#
#        partId = "%d-%d" %(off,off+steps-1)
#        np.savetxt("u_avg_%03d_part_%s.txt" %(j, partId), u_avg)


def main():
    """
    The script can get be started with different argument configurations:
    - u_bar_vtk.py files.dat startLine #numFiles procsStart procsEnd
    #====================================================================
    files.dat: the total list of files to process
    startLine: the line in files.dat from which to start
    #numFiles: the number of files to process from the start
    procsStart: the processor idx to start with
    procsEnd: the processor idx to end with
    """

    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filePattern", help="Pattern for the file series to process. Has to be put into \"\" on Bash, etc... to stop expansion.")
    parser.add_argument("-p", "--procs", help="Here we specify which processor output to process: 1 -> processor 1 OR 3-5 processors 3 to 5")
    args = parser.parse_args()

    print(args.filePattern)
    print(args.procs)
    print(len(args.procs.split("-")))

    if args.filePattern:
        res = glob.glob(args.filePattern)
        res.sort()
        print(res)
        #print(os.getcwd())
    
    if args.procs:
        valProcs = args.procs.split("-")
        procs = len(valProcs)
        if procs > 1:
            procsStart = int(valProcs[0])
            procsEnd   = int(valProcs[1])

    print("%d %d %d" %(procsStart, procsEnd, len(res)))

    processListProcs(res, procsStart, procsEnd)

#    if len(sys.argv) <= 1:
#        print(sys.argv)
#        files = r'd:\work\avg\main.*.pvtu'
#        res = glob.glob(files)
#        steps = len(res)
#        #processFiles(res, steps, 2)
#    else:
#        print("here")
#        #processFileList(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
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

if __name__ == "__main__":
    main()
