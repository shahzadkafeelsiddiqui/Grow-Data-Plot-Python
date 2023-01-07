# Importing libraries
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Initializing list
lattitudelist = []
longitudelist = []
t = 1
# Reading the Grow File
with open('GrowLocations.csv', 'r') as read_obj:
    #Pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    #Iterate over each row in the csv using reader object
    for row in csv_reader:
        #Row variable is a list that represents a row in csv
        latitude = row[1]
        longitude = row [2]
        try:
            latitudefloat = (float(latitude))
            longitudefloat = (float(longitude))
            
            #Minimizing the abnormalities and error values from the CSV file and appending them in a Dataframe
            if ((latitudefloat <= 1.6848 and latitudefloat >= -10.592) and (longitudefloat <= 57.985 and longitudefloat >= 50.681)):
                lattitudelist.append(latitudefloat)
                longitudelist.append(longitudefloat)
                
        except ValueError:
            a = 0
#Creating the final Dataframe
df = pd.DataFrame(list(zip(lattitudelist, longitudelist)),
               columns =['Lattitude', 'Longitude'])
print(df)

#Visualization of the Dataframe on the given map
ruh_m = plt.imread('map7.png')
BBox = (-10.5, 2, 50.8, 58)
fig, ax = plt.subplots(figsize = (10,6))
ax.scatter(df.loc[:,"Lattitude"],df.loc[:,"Longitude"],  zorder=1, alpha= 0.4, c='b', s=10)
ax.set_title('Plotting Grow Data on United Kingdom Map')
ax.set_xlim(-10.5,2)
ax.set_ylim(50.8,58)
ax.margins(x=0)
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
plt.show()