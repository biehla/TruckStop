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
print(carID)

latitude_car1[0] = latitude_car2[0] = latitude_car3[0] = latitude_car4[0] = latitude_car5[0] = latitude_car6[0] = latitude_car7[0] =  latitude_car8[0] =  latitude_care9[0] =  latitude_car10[0] = latitude_car11[0] = 0

code_car1[0] = code_car2[0] = code_car3[0] = code_car4[0] = code_car5[0] = code_car6[0] = code_car7[0] = code_car8[0] = code_car9[0] = code_car10[0] = code_car11[0] = 0

print("Initializing Data...")

a = b = c = d = e = f = g = h = g = k = l = m = n = o = 0

for i in range(len(carID)):
    if carID[i] == "1088214034":
        latitude_car1[a] = data[i,0]
        longitude_car1[a]  = data[i,1]
        code_car1[a] = data[i,4]
        a = a + 1
    if carID[i] == "1088214042":
        latitude_car2[b] = data[i,0]
        longitude_car2[b]  = data[i,1]
        code_car2[b] = data[i,4]
        b = b + 1
    if carID[i] == "1088214013":
        latitude_car3[c] = data[i,0]
        longitude_car3[c]  = data[i,1]
        code_car3[c] = data[i,4]
        c += 1
    if carID[i] == "1088217019":
        latitude_car4[d] = data[i,0]
        longitude_car4[d]  = data[i,1]
        code_car4[d] = data[i,4]
        d += 1
    if carID[i] == "1088217018":
        latitude_car5[e] = data[i,0]
        longitude_car5[e]  = data[i,1]
        code_car5[e] = data[i,4]
        e += 1
    if carID[i] == "1084068100":
        latitude_car6[f] = data[i,0]
        longitude_car6[f]  = data[i,1]
        code_car6[f] = data[i,4]
        f += 1
    if carID[i] == "1084068111":
        latitude_car7[g] = data[i,0]
        longitude_car7[g]  = data[i,1]
        code_car7[g] = data[i,4]
        g += 1
    if carID[i] == "1084067241":
        latitude_car8[h] = data[i,0]
        longitude_car8[h]  = data[i,1]
        code_car8[h] = data[i,4]
        print("AYY")
        h += 1
        
    if carID[i] == "1088214007":
        latitude_car9[j] = data[i,0]
        longitude_car9[j]  = data[i,1]
        code_car9[j] = data[i,4]
        j += 1
    if carID[i] == "1088214034":
        latitude_car10[r] = data[i,0]
        longitude_car10[r]  = data[i,1]
        code_car10[r] = data[i,4]
        r += 1
    if carID[i] == "1088214236":
        latitude_car11[p] = data[i,0]
        longitude_car11[p]  = data[i,1]
        code_car11[p] = data[i,4]
        p += 1


print("...Done")
print( carID[1])

#if():
#    print("TRUE")



# fig = plt.figure(figsize=(20,20))

# m = Basemap(projection = 'lcc', resolution = None, width = 8E6, height = 8E6, lat_0 = 45, lon_0=-100)
# m.etopo()
# #m.bluemarble()

# # MAP

# for rows in range (len(longitude)-9000):
#     x,y = m(longitude[rows], latitude[rows])
#     print("plotting  x:" ,x, " y: ", y)
#     plt.plot(x,y, 'ok', markersize=5)
    

# matplotlib.use('TkAgg')

# plt.show()

