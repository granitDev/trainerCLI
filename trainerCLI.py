import configparser
import sys
import getopt
from random import randint
import datetime
from collections import defaultdict

exConfig = configparser.ConfigParser()
exConfig.read("exercises.ini")

g_now = datetime.datetime.now()

#for arg in sys.argv:
g_exList = []

g_logList = []
g_lastLog = []

#g_exList = defaultdict(list)

def getLastLog(logList):
    lastWorkout = []
    for line in reversed(logList):
        if "@" in line:
            break
        lastWorkout.append(line)
    return list(reversed(lastWorkout))

try:
    with open("training.log","r") as L:
        for line in L:
            line = line[:-1]
            g_logList.append(line)
        g_lastLog = getLastLog(g_logList)
        if len(g_lastLog ) == 0:
            g_lastLog = [x for x in range(100)]
except (OSError, IOError) as e:
    print(e)
    print("Log file not found")
    open("training.log", "w+").close()

def getRandEx(exList):
    return exList[randint(0, (len(exList)-1))]

def getNext(sec, ex, loc):
    exList = []
    for item in exConfig[sec]:
        if loc in exConfig[sec][item]:
            exList.append(item)
    if ex not in exList or exList.index(ex) == len(exList)-1:
        return exList[0]
    else:
        return exList[exList.index(ex)+1]

def getArms(location):
    global exConfig, g_lastLog
    exList = []
    exercise = ""
    
    for sec in exConfig.sections():
        if sec == "arms.push":
            exercise = getNext(sec, g_lastLog[0], location)
            exList.append(exercise)
        elif sec == "arms.pull":
            exercise = getNext(sec, g_lastLog[1], location)
            exList.append(exercise)
        elif sec == "arms.curl":
            exercise = getNext(sec, g_lastLog[2], location)
            exList.append(exercise)
    
    return exList
    
def buildWorkout(site):
    global exConfig, g_now, g_lastLog
    exList = []
    
    for ex in getArms(site):
        exList.append(ex)
        
    for sec in exConfig.sections():
        if "hand" in sec:
            exList.append(getNext(sec, g_lastLog[3], site))
        if "leg" in sec:
            exList.append(getNext(sec, g_lastLog[4], site))
            #g_exList.append(exConfig[sec].get(exercise))
    with open("training.log","a+") as f:
        f.write("@ {}\n".format(g_now.strftime("%Y-%m-%d %A")))
        print("@ {}".format(g_now.strftime("%Y-%m-%d %A")))
        for ex in exList:
            f.write("{}\n".format(ex))
            print("{}".format(ex))

buildWorkout("gym")
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
