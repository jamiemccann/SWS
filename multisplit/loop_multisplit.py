# -*- coding: utf-8 -*-

import os 
import glob
from pathlib import Path
import obspy


def run_msplit(dir_path):
    """
    Function to run multisplit on a directory filled with sac files.
    These sac files must be in the correct format. This format is a directory (dir_path), containing
    directories for each event-station pair, and in each directory there should be a east and north component sac file
    for that event-station pair.


    Parameters

    dir_path: str, directory containing the data
    
    """
    directory = Path(dir_path).iterdir()
    for event_station in directory:
        
        
        n_comp = glob.glob(f'{event_station}/*.n')
        e_comp = glob.glob(f'{event_station}/*.e')


        
        os.system(f'/raid2/jam247/ftilmann_split/multisplit/multisplit -data {n_comp[0]} {e_comp[0]} -me -winp b e -single 1 0.0125 0.6')        

            
            
            
