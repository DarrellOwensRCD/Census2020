import json
import csv
import statistics
import os.path
from os import path
def main():
    write = 0
    final = 0
    filename = '/Users/darrell/Downloads/ca2020.pl/ca000012020.pl'
    filename2 = '/Users/darrell/Downloads/ca2020.pl/ca000022020.pl'
    geoname = '/Users/darrell/Downloads/ca2020.pl/cageo2020.pl'
    destfile = '/Users/darrell/Desktop/Census2020/AllCACities2020Census.csv'
    d = open(filename, encoding = "ISO-8859-1")
    d2 = open(filename2, encoding = "ISO-8859-1") #Housing File
    g = open(geoname,encoding = "ISO-8859-1" )
    e = open(destfile, encoding = "ISO-8859-1")
    dest_line = csv.reader(e, delimiter=',')
    csv_dest = list(dest_line)
    e.close()
    Lines = d.readlines()
    Lines2 = d2.readlines()
    Geo_Lines = g.readlines()
    row = 1
    pop = 0
    white = 0
    black = 0
    asian = 0
    latino = 0
    GEO_ID = 0
    #Step 1, iterate through each city in California
    print("Starting...")
    for geoline in Geo_Lines:
        arr = geoline.split("|")
        if(38426 == int(arr[7])): #we're done
            print("WE ARE DONE")
            break
        if(36815 <= int(arr[7])): #STep 2 if we find the proper GEO ID
            GEO_ID = arr[7]
            city_name = arr[86]
            for line in Lines:
                array = line.split("|")
                if(array[4] == GEO_ID):
                    #print("Found")
                    if(arr[87] == arr[86] + " CDP"):
                        city_name = city_name + " (unincorporated place)"
                    line.split("|")
                    #print(city_name)
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
                    for line2 in Lines2:
                        array2 = line2.split("|")
                        if(array2[4] == GEO_ID): #Step 2.5 Add the housing units from File 2
                            csv_dest[row][11] = int(array2[149]) #housing units
                            csv_dest[row][12] = int(array2[150]) #Occupieds 
                            csv_dest[row][13] = int(array2[151]) #Vacants
                            break
                    break
            row += 1
    my_new_list = open(destfile, 'w') #opening write file
    csv_writer = csv.writer(my_new_list) #write everything and close out
    csv_writer.writerows(csv_dest)
    my_new_list.close()
    d2.close()
    d.close()
    g.close()
