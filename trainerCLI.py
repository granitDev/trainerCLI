import configparser
import sys
import getopt
from random import randint

exConfig = configparser.ConfigParser()
exConfig.read("exercises.ini")

#for arg in sys.argv:
g_exList = []
    
def getExerises():
    global g_exList
    for sec in exConfig.sections():
        if "arm" in sec:
            tmp = []
            for item in exConfig[sec]:
                tmp.append(item)
            rnd = randint(0, (len(tmp)-1))
            g_exList.append(tmp[rnd])
    print(g_exList)

getExerises()
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
