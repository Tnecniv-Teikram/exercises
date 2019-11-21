# This is a test document solely for the purpose of learning Python. 24.10.2019

station_name = "Helsinki Kaivopuisto"
station_id = 132310
station_lat = 24.96 

# create a list of metro stops
station_names = ['Helsinki Harmaja', ' Helsinki Kaisaniemi',' Helsinki Kaivopuisto','Helsinki Kumpula']

# create list of station types and modify list at index value
station_types = ['weather stations','weather stations','weather stations','weather stations']
station_types[2] = 'Mareographs'

station_type = 'Mareographs'

# store variiables in a list 
station_hel_kaivo = [station_name, station_id, station_lat,station_lat,station_type]
print(station_hel_kaivo)

# delete variable at specified index value
# del station_names[5]
# print(station_names)

station_names.append('Helsinki lighthouse')

# count the number of occurences of a value
station_names.count('Helsinki Kumpula')

# count the index value of an item in a list
station_names.index('Helsinki Kumpula')

# reversing a list 
station_names.reverse()

# sorting a list 
station_names.sort()


