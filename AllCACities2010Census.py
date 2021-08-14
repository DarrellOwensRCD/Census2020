import csv
def main():
    write = 0
    final = 0
    sourcefile = '/Users/darrell/Desktop/Census2020/nhgis0045_csv/nhgis0045_ds171_2010_place.csv' #source
    destfile = '/Users/darrell/Desktop/Census2020/AllCACities2020Census.csv' #End destination
    d = open(sourcefile, encoding = "ISO-8859-1")
    e = open(destfile, encoding = "ISO-8859-1")
    file_line = csv.reader(d,  delimiter=',')
    dest_line = csv.reader(e, delimiter=',')
    source_rows = list(file_line)
    dest_rows = list(dest_line)     
    e.close()
    d.close()
    print("Cooking...")
    #Run through Dest file and check source file for corresponding names
    for city_name in dest_rows: #get the name from the destination csv
        checkname = 0 #declaring var to hold the string. If current city is incorporated, check that
        if(city_name[1] == "unincorporated place"): #if dest file city is unincorporated, require that for 2010
            checkname = city_name[0] + " CDP"
        else:
            checkname = city_name[0]
        for search in source_rows: #run the name by the source Census sheet
            if(search[4] == "California"): #if search is in California...
                if(checkname == search[8] or search[8] == checkname + " city"  or search[8] == checkname + " town"):
                    #If found, input the 2010 data into the sheet
                    city_name[14] = city_name[0] #name
                    if(checkname == city_name[0] + " CDP"):
                        city_name[15] = "unincorporated place"
                    else:
                        city_name[15] = "incorporated place"
                    city_name[16] = int(search[33])#population
                    city_name[17] = int(search[34])#latino
                    city_name[18] = int(search[37])#white
                    city_name[19] = int(search[38])#black
                    city_name[20] = int(search[39])#native
                    city_name[21] = int(search[40])#asian
                    city_name[22] = int(search[41])#pacific
                    city_name[23] = int(search[42])#other
                    city_name[24] = int(search[43])#multi-race
                    city_name[25] = int(search[106])#units
                    city_name[26] = int(search[107])#occupied
                    city_name[27] = int(search[108])#vacant
                    #print(city_name)
                    break     
    my_new_list = open(destfile, 'w') #opening write file
    csv_writer = csv.writer(my_new_list) #write everything and close out
    csv_writer.writerows(dest_rows)
    my_new_list.close()
    print("DONE!")
