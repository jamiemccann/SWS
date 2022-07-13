# -*- coding: utf-8 -*-



import obspy
from obspy import read
import glob
import re
import os
import shutil
import pathlib



def qm_2_multisplit(pat: str):
    """
    
    Function to convert directory from quakemigrate output standard to multisplit standard structure

    Parameters

    pat: str, Path of directory containing sac files
    
    
    """

    all_files = [filename for filename in glob.glob(f'{pat}/**/**/*.n')]
    all_files.extend([filename for filename in glob.glob(f'{pat}/**/**/*.e')])

    

    def get_full_path(file):
        try:
            event = file
            event_station_inter = file.split('/')[-1].split('.')[0:2]
            sep = '.'
            event_station = sep.join(event_station_inter)
        except:
            event_station = 'Erroneous Data'
        

        event_station_folder = f'{event_station}/'
        file_path = f'{event}'

        return event_station_folder, file_path 

    #Create empty station folder and full_path lists
    event_station_folders = []
    full_paths = []


    for file in all_files:
        event_station_folder, full_path = get_full_path(file)
        event_station_folders.append(event_station_folder), full_paths.append(full_path)


    #Create the station folders
    for i in range(len(all_files)):
        os.chdir(pat)
        os.makedirs(event_station_folders[i], exist_ok=True)
        os.rename(all_files[i], full_paths[i])

    for file in full_paths:
        try:
            source_path = file
            destination_path = file.split('/')[-1][:-2]
            shutil.copy(source_path, destination_path)
            #print(f'copying {file} from {source_path} to {destination_path}')
        except:
            print(f"Error with {file}, destination path doesn't exist")
            pass

    old_folders = []

    for i in glob.glob(f'{pat}/**'):
        if i[-1]=='0':
            old_folders.append(i)





    
