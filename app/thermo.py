import json
from flask import url_for
import os
import sys



def getProp(data, T, prop):
    Tmin = max(filter(lambda x: x <= T, data["T"]))
    xMin = data["T"].index(Tmin)
    Tmax = min(filter(lambda x: x>= T, data["T"]))
    xMax = data["T"].index(Tmax)

    propMin = data[prop][xMin]
    propMax = data[prop][xMax]
    
    if Tmin != Tmax:
        return(linearInterpolate(Tmin, Tmax, propMin, propMax, T))
    else:
        return(propMin)
    




def getAllProps(data, T):
    values = {}
    for prop in (data["labels"]):
       values[prop] = getProp(data, T, prop) 
    return(values)





def linearInterpolate(x1, x2, y1, y2, x):
    slope = (y2-y1)/(x2-x1)
    return(y1 + slope*x)
            



def getThermoData(filepath, T):
    data = {}
    print (os.getcwd()) # python 3
    print("This is the name of the program:", sys.argv[0])
    print("Argument List:", str(sys.argv))
    files = [ f for f in os.listdir( os.curdir+"/app/Data" ) ] #list comprehension version.
    print(files)
    sys.stdout.flush()
    file = os.curdir+"/app/Data/water.json"
    with open(file) as json_file:
        tmp = json.load(json_file)
        data.update(tmp)
    return(getAllProps(data, T))







    