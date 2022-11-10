# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
This script generates re-organises the output of QM2MFAST to allow for 
quick useage of MFAST by organising data in folders of stations, as opposed to folders of events.
The structure will change
Needs to be run in the same directory as the event-station folders
Initial:
>Single_event
    >Stations detected
        >component sac files for station-event pair
After this code:
>Stations
    >component sac files for station-event pair
This allows the use of ./do_station_mfm in with mfast
"""



import os 
import glob
import shutil
import re
import pandas as pd
import pathlib




#Collect all files in the directory created into a single list 
all_files = [filename for filename in glob.glob('/raid2/jam247/mfast/sample_data/Post_Inflation_Run/**/*.e', recursive=True)]
all_files.extend([filename for filename in glob.glob('/raid2/jam247/mfast/sample_data/Post_Inflation_Run/**/*.n', recursive=True)])
all_files.extend([filename for filename in glob.glob('/raid2/jam247/mfast/sample_data/Post_Inflation_Run/**/*.z', recursive=True)])

#Create fucntion to get full paths for events and stations 
def get_full_path(file):
    try:
        event = file
        station = file.split('.')[1]
    except:
        station = 'Erroneous Data'
    

    station_folder = f'{station}/'
    file_path = f'{event}'

    return station_folder, file_path





    
#Create empty station folder and full_path lists
station_folders = []
full_paths = []


#Append full paths and stations into station_folders list and full_paths list
for file in all_files:
    station_folder, full_path = get_full_path(file)
    station_folders.append(station_folder), full_paths.append(full_path)



#loop through files and copy files into new station folder paths 
for file in full_paths:
    try:
        source_path = file
        #print(source_path)
        station = file.split('/')[7]
        #print(station)
        destination_path = str(pathlib.Path(file).resolve().parent.parent.parent) + '/' +f'{station}'
        #print(str(destination_path))
        print(f'Moving {source_path} to {destination_path}')
        shutil.copy(source_path,destination_path)
    except:
        pass
