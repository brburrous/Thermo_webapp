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
            



def getThermoData(material, T):
    data = {}
    file = os.curdir+"/app/Data/"+material.lower()+".json"
    with open(file) as json_file:
        tmp = json.load(json_file)
        data.update(tmp)
    return(getAllProps(data, T))







    