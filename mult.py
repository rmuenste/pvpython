import sys
import os

def main():
    print(sys.argv)
    fileName = sys.argv[1]
    outName  = sys.argv[2]

    with open(fileName) as f:
        for line in f.readlines():
            words = line.split()
            with open(outName, "a") as o:
                outString = "%s %.16f\n" %(words[0], float(words[1]) * 1.059)
                o.write(outString)
                print (words[0], float(words[1]) * 1.059)

if __name__ == "__main__":
    main()