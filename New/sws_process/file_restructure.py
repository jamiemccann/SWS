# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
This script generates re-organises the output of QM2MFAST to allow for 
quick useage of MFAST by organising data in folders of stations, as opposed to folders of events.



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



def restructure(pat):
    """
    This function restructures the directories so that they are useable by MFAST
    """

    #Collect all files in the directory created into a single list 
    all_files = [filename for filename in glob.glob(f'{pat}/**/*.e', recursive=True)]
    all_files.extend([filename for filename in glob.glob(f'{pat}/**/*.n', recursive=True)])
    all_files.extend([filename for filename in glob.glob(f'{pat}/**/*.z', recursive=True)])



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
            destination_path = file.split('/')[7] + '/'
            shutil.copy(source_path, destination_path)
        except:
            pass




    #finally we want to get rid of the old data 
    old_folders = []
    for i in glob.glob(f'{pat}/**'):
        if i.split('/')[-1][0]== '2': #all of these folder names will have begin with 2, as they are from the year 2000 beyond
            old_folders.append(i)
    print(old_folders)
    

    for folder in old_folders:
        shutil.rmtree(folder)
