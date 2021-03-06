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




#Collect all files in the directory created into a single list 
all_files = [filename for filename in glob.glob('**/*.e', recursive=True)]
all_files.extend([filename for filename in glob.glob('**/*.n', recursive=True)])
all_files.extend([filename for filename in glob.glob('**/*.z', recursive=True)])



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


#Create the station folders
for i in range(len(all_files)):
    os.makedirs(station_folders[i], exist_ok=True)
    os.rename(all_files[i], full_paths[i])



#loop through files and copy files into new station folder paths 
for file in full_paths:
    try:
        source_path = file
        destination_path = file.split('/')[1] + '/'
        shutil.copy(source_path, destination_path)
    except:
        pass




#finally we want to get rid of the old data 
old_folders = []
for i in os.listdir():
    if len(i) == 17: #all of these folder names will have 17 characters, stations will never have this many characters
        old_folders.append(i)


for folder in old_folders:
    shutil.rmtree(folder)
