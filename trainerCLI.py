import configparser
import sys
import getopt
from random import randint

exConfig = configparser.ConfigParser()
exConfig.read("exercises.ini")

#for arg in sys.argv:
g_exList = []

def getRandEx(exList):
    return exList[randint(0, (len(exList)-1))]

def getExerise(section):
    global exConfig
    lastList = []
    exList = []
    exercise = ""
    try:
        with open("last.log","r") as f:
            for line in f:
                line = line[:-1]
                lastList.append(line)
    except (OSError, IOError) as e:
        print(e)
        
    for item in exConfig[section]:
        exList.append(item)
    exercise = getRandEx(exList)
    while exercise in lastList:
        #print("last: ", exercise)
        exercise = getRandEx(exList)
    return exercise
    
def buildWorkout():
    global g_exList, exConfig
    for sec in exConfig.sections():
        if "arm" in sec:
            g_exList.append(getExerise(sec))
        if "hand" in sec:
            g_exList.append(getExerise(sec))
        if "leg" in sec:
            g_exList.append(getExerise(sec))
            #g_exList.append(exConfig[sec].get(exercise))
    with open("last.log","w+") as f:
        for ex in g_exList:
            f.write("%s\n" % ex)
            print(ex)

buildWorkout()
exit()

def main(argv):
    try:
        # g gym, h home, 
        opts, args = getopt.getopt(argv, "hg:m:", ["help", "gym=", "home="])
    except getopt.GetoptError:
        usage()
        sys.exit(-1)
        
if __name__ == "__main__":
    main(sys.argv[1:])
