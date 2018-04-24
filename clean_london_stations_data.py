# let's grab the data from the downloaded file
# if you don't have fastkml, you will need to run
# `pip3.6 install --user fastkml`

from fastkml import kml
with open('datasets/stations.kml', 'rb') as data_file:
    data_string = data_file.read()
k = kml.KML()
k.from_string(data_string)
# some crazy nested stuff to get to the stations through some generators. feel free to not undestand this line
stations_raw = list(list(k.features())[0].features())

# print out the first 5 stations just as a sanity check
for station in stations_raw[:5]:
    # a type of pygeoif.geometry.Point
    point = station._geometry.geometry
    print(station.name, point.x, point.y)

# lets put them into pandas dataframes
import pandas as pd

stations_list = [{
    'station_name': s.name,
    'coordinate-x': s._geometry.geometry.x,
    'coordinate-y': s._geometry.geometry.y
} for s in stations_raw]

stations = pd.DataFrame(stations_list)

# again, let's sanity check we have the right stuff
print(stations.head())

stations.to_hdf('./datasets/london_stations_python2.h5', key='stations')
