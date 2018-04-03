import configparser

exConfig = configparser.ConfigParser()
exConfig.read("exercises.ini")

for sec in exConfig.sections():
    print(sec)
    for item in exConfig[sec]:
        print("    ", item)