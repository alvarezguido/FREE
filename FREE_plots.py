#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 09:06:30 2020

@author: guido
"""

import matplotlib.pyplot as plt
import math
import numpy as np

def read_data(file):
    data = []
    sf_dist = []
    slot_length = []
    frame_length = []
    guards = []
    with open(file) as file:
        data_lines = file.readlines()
    for line in data_lines:
        data_line = line #depreciate line 0
    data = data_line.split(" ")
    for i in data[16:22]:
        sf_dist.append(int(i))
    for i in data[22:28]:
        slot_length.append(float(i))
    for i in data[28:34]:
        frame_length.append(float(i))
    for i in data[34:40]:
        guards.append(float(i))
    print ("Collection time: ", float(data[10]), "[s]")
    print ("Number of Random Seeds: ",data[0])
    print ("Average sending interval per end-device, in miliseconds: ", data[1], "[ms]")
    print ("N° of end-devices simulated: ",data[2])
    print ("Buffer of data to be send for each end-device: ", float(data[3]), "Bytes")
    print ("Total Sent packets: ", data[4])
    print ("Total number of packets collisions: ", data[5])
    print ("Total lost packets: ", data[6])
    print ("Total lost packets because CRC bad check: ", data[7])
    print ("No ACK packets: ", data[8])
    print ("ACK Lost packets number: ",data[9])
    print ("DER: ", data[10])
    print ("DER method 2: ", data[11])
    print ("Overall Energy consumption: ", float(data[12]), "[J]")
    watts = float(data[12]) / float(data[10])
    print ("Energy consumption in mili Watts: ", watts*1000, "[mW]")
    print ("Energy consumption in dBm: ", 10*math.log10(watts*1000), "[dBm]")
    
    
    return data, sf_dist, slot_length, frame_length, guards

data_file = "confirmabletdmaTX.dat"

data, sf_dist, slot_length, frame_length, guards = read_data(data_file)

#fig = plt.figure(figsize=(12, 5), dpi= 80, facecolor='w', edgecolor='k')
#fig = plt.figure(1)
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
fig = plt.subplot(2,2,1)
x = ["SF7","SF8","SF9","SF10","SF11","SF12"]
#y_pos = np.arange(len(x))
plt.bar(x, sf_dist, color="r", width=0.25)
plt.title('SF Distribution')
plt.xlabel('Spreading Factor')
plt.ylabel('N° of end-devices')
#yint = range(min(sf_dist), math.ceil(max(sf_dist))+1)
#plt.yticks(yint)
#plt.grid()
plt.show()

#fig = plt.figure(3)
fig = plt.subplot(2,2,2)
y_pos = np.arange(len(x))
plt.bar(x, guards, color="y", width=0.25)
plt.title('Number of Guards slots per SF frame')
plt.xlabel('Spreading Factor')
plt.ylabel('N° of Guards per SF')
#yint = range(min(guards), math.ceil(max(guards))+1)
#plt.yticks(yint)
plt.grid()
plt.show()

#plt.figure(2)
fig = plt.subplot(2,2,3)

plt.bar(x, slot_length, color="b", width=0.25)
#SLOT DURATION IS THE TIME OF EACH SLOT IN THE CORRESPONDED FRAME
#REMEMBER THERE IS ONE CERTAIN FRAME PER SF
plt.title('Slot Duration per SF')
plt.xlabel('Spreading Factor')
plt.ylabel('Time Duration in seconds [s]')
#yint = range(min(slot_length), math.ceil(max(slot_length))+1)
#plt.yticks(yint)
plt.grid()
plt.show()

fig = plt.subplot(2,2,4)
plt.bar(x, frame_length, color="g", width=0.25)
#FRAME IS COMPOSED OF SEVERAL SLOTS, PER SF
#EACH FRAME HAS 1 SLOT (UL) PER END-DEVICE ON THAT SF, + 1 SLOT DL
#EXAMPLE: IF 2 END-DEVICES USES SF:8 => FRAME:3 SLOTS
plt.title('Frame Duration per SF')
plt.xlabel('Spreading Factor')
plt.ylabel('Time Duration in seconds [s]')
#yint = range(min(slot_length), math.ceil(max(slot_length))+1)
#plt.yticks(yint)
plt.grid()
plt.show()


