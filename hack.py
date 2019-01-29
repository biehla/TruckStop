#!/usr/bin/python

import numpy as np
import csv
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import pandas
colnames = ['lat', 'lon', 'typ', 'date', 'code']
data1 = pandas.read_csv('Data_From_Cargo.csv', names=colnames)

with open('Data_From_Cargo.csv', 'rb') as csvFile:
    data = np.genfromtxt(csvFile, delimiter=',')

typ = data1.typ.tolist()
lat = data1.lat.tolist()
lon = data1.lon.tolist()

carID  = typ

print("Total Values Found in  ", range(len(carID)))


latitude_car1 = latitude_car2 = latitude_car3 = latitude_car4 = latitude_car5 = latitude_car6 = latitude_car7 =  latitude_car8 =  latitude_care9 =  latitude_car10 = latitude_car11 = []

longitude_car1 = longitude_car2 = longitude_car3 = longitude_car4 = longitude_car5 = longitude_car6 = longitude_car7 =  longitude_car8 =  longitude_care9 =  longitude_car10 = longitude_car11 = []


code_car1 = code_car2 = code_car3 = code_car4 = code_car5 = code_car6 = code_car7 = code_car8 = code_car9 = code_car10 = code_car11 = []

print("Initializing Data...")

for i in range(len(carID)):
    if carID[i] == "1088214034":
        latitude_car1.append(data[i,0])
        longitude_car1.append(data[i,1])
        code_car1.append(data[i,4])
    elif carID[i] == "1088214042":
        latitude_car2.append(data[i,0])
        longitude_car2.append(data[i,1])
        code_car2.append(data[i,4])
    elif carID[i] == "1088214013":
        latitude_car3.append(data[i,0])
        longitude_car3.append(data[i,1])
        code_car1.append(data[i,4])
    elif carID[i] == "1088217019":
        latitude_car4.append(data[i,0])
        longitude_car4.append(data[i,1])
        code_car4.append(data[i,4])
    elif carID[i] == "1088217018":
        latitude_car5.append(data[i,0])
        longitude_car5.append(data[i,1])
        code_car5.append(data[i,4])
    elif carID[i] == "1084068100":
        latitude_car6.append(data[i,0])
        longitude_car6.append(data[i,1])
        code_car6.append(data[i,4])
    elif carID[i] == "1084068111":
        latitude_car7.append(data[i,0])
        longitude_car7.append(data[i,1])
        code_car7.append(data[i,4])
    elif carID[i] == "1084067241":
        latitude_car8.append(data[i,0])
        longitude_car8.append(data[i,1])
        code_car8.append(data[i,4])
    elif carID[i] == "1088214007":
        latitude_car9.append(data[i,0])
        longitude_car9.append(data[i,1])
        code_car9.append(data[i,4])
    elif carID[i] == "1088214034":
        latitude_car10.append(data[i,0])
        longitude_car10.append(data[i,1])
        code_car10.append(data[i,4])
    elif carID[i] == "1088214236":
        latitude_car11.append(data[i,0])
        longitude_car11.append(data[i,1])
        code_car11.append(data[i,4])


print("...Done")
print( carID[1])


# Make a map of all the data points on the globe

fig = plt.figure(figsize=(20,20))

m = Basemap(projection = 'lcc', resolution = None, width = 8E6, height = 8E6, lat_0 = 45, lon_0=-100)
m.etopo()
#m.bluemarble()

# MAP
for rows in range (len(longitude_car8)):
    x,y = m(longitude_car8[rows], latitude_car8[rows])
    print("plotting  x:" ,x, " y: ", y)
    plt.plot(x,y, 'ok', markersize=5)
    

matplotlib.use('TkAgg')

plt.savefig('PlottedData.png')

