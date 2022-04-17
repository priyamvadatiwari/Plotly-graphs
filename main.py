
import json
from datetime import datetime
import matplotlib.pyplot as plt
from plotly.graph_objects import Bar, layout


'''Pick two places and download temperature data and time for both create a dictionary using the following format temps = {“time”:[],“place1”:[],”place2”:[]} and save this data to a json file called temps.json. In order to match up, you will need to write the time, then the two temps, and repeat. Log enough data that you are able to do an analysis over time (Minimum 5 days of data). Read the JSON file and create a graph with labels showing both sets of temperature data (y-axis) and time series (x-axis), make sure to include labels for the chart, x and y axes.'''

import csv
   
# csv file used is dataexport_Sudbury-Jax-DateTime.csv
filename="dataexport_Sudbury-Jax-DateTime.csv"
temps = {}
# opening the file using "with"
# statement
with open(filename) as file_object:
  reader = csv.reader(file_object)
  header_row = next(reader)
  temps['time'] = [rows[0] for rows in reader] 

#Sudbury temperatures into dictionary
with open(filename) as file_object:
  reader = csv.reader(file_object)
  header_row = next(reader)
  temps['Greater Sudbury'] = [rows[1] for rows in reader] 

#Jacksonville temperatures into dictionary
with open(filename) as file_object:
  reader = csv.reader(file_object)
  header_row = next(reader)
  temps['Jacksonville'] = [rows[2] for rows in reader] 
  
#save the dictionary to json. 
with open('temps.json', 'w') as jsonFile:
  jsonFile.write(json.dumps(temps, indent=0))

#read the json file.
filename = 'temps.json'
with open(filename) as f:
  all_temp_data = json.load(f)

timestamps, Sudburys, Jacksonvilles = [], [], []

timestamps = temps['time']
Sudburys = temps['Greater Sudbury']
Jacksonvilles = temps['Jacksonville']

#Plotting
fig, ax = plt.subplots()
ax.plot(timestamps,Sudburys, c="red",alpha=0.5)
ax.plot(timestamps, Jacksonvilles, c = "green",alpha=0.5)

#Formating the plot

plt.title("Temperatures of Sudbury, ON and Jacksonville FL", fontsize = 15)
plt.xlabel("Date Time",  fontsize = 12)
plt.ylabel("Temperatures (C)",fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 9)
fig.autofmt_xdate()

# Saving the plot
plt.savefig("Sudbury-Jax-Temperatures.jpg")


'''Generate a  visualization using synthetically generated data of your choice (not weather related , could be csv or json).

revenueHistoryFile = "Revenue History.csv"
revenues = []
with open(revenueHistoryFile) as file_object:
  reader = csv.reader(file_object)
  header_rows = next(reader)
  # print(header_rows)

#read the revenues and load them in the list
  for row in reader:
    revenue = row[2]
    revenues.append(revenue)
 
#Create a plot for revenues
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(revenues, c="red")

#Plot Formating
plt.title("Revenue in Millions",fontsize = 10)
plt.xlabel('xdfd',fontsize = 6)
plt.ylabel('Revenues', fontsize = 6)
plt.tick_params(axis = "both", which = "major", labelsize = 6)
fig.autofmt_xdate()
plt.show()'''


'''Use Earthquake.csv (attached) and create a Scattergeo visualization using Plotly, which shows the magnitudes of all the earthquakes in the csv file. Use the fields latitude and longitude from within the csv to plot the locations.'''

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#read the csv file
filename_eq = 'Earthquake.csv'
with open(filename_eq) as file_object:
  reader_eq = csv.reader(file_object)
  header_row = next(reader_eq)
  #print(header_row)
  for i,col_header in enumerate(header_row):
    print(i,col_header)
  #create empty list to import data from csv file.
  mags, lons, lats = [], [], []

  #import the data in the list of the columns that are required. 
  for row in reader_eq:
    mag = float(row[4])
    lon = float(row[2])
    lat = float(row[1])
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
  
  #Map the earthquakes
  data = [{
  "type": 'scattergeo',
  "lat": lats, 
  "lon": lons,
  "marker": {
    "size": [5*mag for mag in mags],
    "color":"pink",
    "colorscale":"Viridis",
    "reversescale":True,
    "colorbar":{"title":"Magnitude"}
    }
  }]
  my_layout = Layout(title = "Earthquakes around the World")

  figure = {'data': data, 'layout': my_layout}
  offline.plot(figure, filename = 'eqMap.html')

'''Use Earthquake.csv (attached) and create a histogram(like we studied last week) of all the depths in the csv file.'''


filename = 'Earthquake.csv'
with open(filename) as file_object:
  reader_dp = csv.reader(file_object)
  header_row = next(reader_dp)

  depths = []

  for row in reader_dp:
    depth = float(row[3])
    depths.append(depth)

  depthdata = [Bar(y=depths)]

xaxis_config = {"title":"Earthquake"}
yaxis_config = {"title":"Frequency - depth"}

my_layout = Layout(title="Depth Histogram", xaxis = xaxis_config, yaxis = yaxis_config)

offline.plot({"data":depthdata,"layout":my_layout},filename = "eqdepth.html")