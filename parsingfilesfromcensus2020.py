import json
import csv
import statistics
import os.path
from os import path
def main():
    bay_file = '__San_Francisco_Bay_Region_Incorporated_Cities_and_Towns.geojson' #list of Bay cities
    write = 0
    final = 0
    filename = '/Users/darrell/Downloads/ca2020.pl/ca000012020.pl'
    geoname = '/Users/darrell/Downloads/ca2020.pl/cageo2020.pl'
    destfile = '/Users/darrell/Desktop/Census2020Cities/Cities2020Census.csv'
    bay_file = '/Users/darrell/Downloads/__San_Francisco_Bay_Region_Incorporated_Cities_and_Towns.geojson' #list of Bay cities
    d = open(filename, encoding = "ISO-8859-1")
    g = open(geoname,encoding = "ISO-8859-1" )
    e = open(destfile, encoding = "ISO-8859-1")
    dest_line = csv.reader(e, delimiter=',')
    csv_dest = list(dest_line)
    e.close()
    Lines = d.readlines()
    Geo_Lines = g.readlines()
    bc = open(bay_file)
    city_name = json.load(bc)
    row = 1
    pop = 0
    white = 0
    black = 0
    asian = 0
    latino = 0
    GEO_ID = 0
    #Step 1, iterate through each city in Bay City
    for feat in city_name['features']:
        city_name = feat["properties"]["jurname"]
        print(city_name)
        #Step 2, match name in geo file to get ID
        for geoline in Geo_Lines:
            arr = geoline.split("|")
            if(city_name == arr[86] and 36815 <= int(arr[7])):
                GEO_ID = arr[7]
                break
        #Step 3, match the GEO ID In the Census File and print race data
        for line in Lines:
            array = line.split("|")
            if(array[4] == GEO_ID):
                print("Found")
                line.split("|")
                csv_dest[row][1] = city_name #Name of City
                csv_dest[row][2] = int(array[76]) #Population
                csv_dest[row][3] = int(array[77]) #Latinos
                csv_dest[row][4] = int(array[80]) #Whites
                csv_dest[row][5] = int(array[81]) #Black
                csv_dest[row][6] = int(array[82]) #Natives
                csv_dest[row][7] = int(array[83]) #Asian
                csv_dest[row][8] = int(array[84]) #Hawaii
                csv_dest[row][9] = int(array[85]) #Other
                csv_dest[row][10] = int(array[86]) #Multiracial
                break
        row += 1
    my_new_list = open(destfile, 'w') #opening write file
    csv_writer = csv.writer(my_new_list) #write everything and close out
    csv_writer.writerows(csv_dest)
    my_new_list.close()
    d.close()
    g.close()
    bc.close()
